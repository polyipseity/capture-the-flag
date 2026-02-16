<?php
error_reporting(0);
if(strpos($_REQUEST['url'],"http")===0){
    $opts = array(
        'http'=>array(
            'method'=>"GET",
            'header'=>$_REQUEST['header'])
        );
        $context = stream_context_create($opts);
        $file = file_get_contents($_REQUEST['url'], false, $context);
        // echo $file; # no show for u
}else{
    echo "hacker!";
}

highlight_file(__FILE__);

?>

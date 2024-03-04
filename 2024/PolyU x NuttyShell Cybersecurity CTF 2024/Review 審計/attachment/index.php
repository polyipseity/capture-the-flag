<?php
if(isset($_POST["submit"])){
    if(!isset($_FILES["file"])){
        die("No file uploaded");
    }
    else if($_FILES["file"]["size"] > 2097152){
        die("File size is too large");
    }
    else if(pathinfo($_FILES["file"]["name"], PATHINFO_EXTENSION) != "zip"){
        die("File extension is not supported");
    }
    else if(file_get_contents($_FILES["file"]["tmp_name"], FALSE, NULL, 0, 2) != "PK"){
        die("File is not a zip file");
    }
    else if(!move_uploaded_file($_FILES["file"]["tmp_name"], "uploads/" . $_FILES["file"]["name"])){
        die("File is not uploaded");
    }
    else{
        $dir = "uploads/" . pathinfo($_FILES["file"]["name"], PATHINFO_FILENAME);
        if(!file_exists($dir)){
            mkdir($dir);
        }
        else{
            die("Directory is already exists");
            return;
        }
        $zip = new ZipArchive;
        $res = $zip->open("uploads/" . $_FILES["file"]["name"]);
        if($res === TRUE){
            for($i = 0; $i < $zip->numFiles; $i++) {
                $filename = $zip->getNameIndex($i);
                $fileinfo = pathinfo($filename);
                copy("zip://"."./uploads/" . $_FILES["file"]["name"]."#".$filename, $dir . "/". $fileinfo['basename']) or die("Unzip failed!");
            }                   
            $zip->close();

            $files = scandir($dir);
            foreach($files as $file){
                if($file != "." && $file != ".."){
                    if(pathinfo($file, PATHINFO_EXTENSION) != "jpg" && pathinfo($file, PATHINFO_EXTENSION) != "png"){
                        unlink($dir . "/" . $file);
                    }
                }
            }

            unlink("uploads/" . $_FILES["file"]["name"]);
            echo "File is uploaded successfully";
        }
    }
}
?>

<html>
    <head>
        <title>Review</title>
    </head>
    <body>
        <h1>Review</h1>
        <p>Submit files here, we will check your file is safe or not?</p>
        <form action="index.php" method="post" enctype="multipart/form-data">
            File:
            <input type="file" name="file" id="file">
            <input type="submit" id="submit" value="Submit" name="submit">
        </form>
    </body>
</html>
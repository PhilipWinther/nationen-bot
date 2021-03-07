<html>
<body>

<div class="divbuttons">


<form action="" form="" method="post">
        <input type="submit" name="randomcommentbutton" class="button" value="Show me 1 random comment" />

        <input type="submit" name="100commentsbutton" class="button" value="Show me 100 random comments" />

        <input type="text" name="search" />
                <input type="submit" name="submit" class="button" value="Search" /></form>

</div>






<?php
        if(array_key_exists('randomcommentbutton', $_POST)) {
            randomcomment();
        }
        elseif(array_key_exists('100commentsbutton', $_POST)) {
            thousandcomments();
        }


        elseif(array_key_exists('search', $_POST)) {
            search1();
        }


        function randomcomment() {
            include 'db.php';
            $maxIDsql = "SELECT MAX(id) FROM comments";
            $maxIDselect = mysqli_query($conn,$maxIDsql);
            $maxIDresult = mysqli_fetch_row($maxIDselect);
            $id =  $maxIDresult[0];
            $random =(rand(1,$id));
            $Aselect = "SELECT * FROM comments where id =$random";
            $result = mysqli_query($conn,$Aselect);
            $result1 = mysqli_query($conn,$Aselect);
//            $urlIDresult = mysqli_fetch_array($result1);
            $urlID = $row[0];

            if (mysqli_num_rows($result) > 0) {
            ?>
            <div class="div-table">
            <div class="trow">
            <div class="tcolumn tcolumn1">ID</div>
            <div class="tcolumn tcolumn2">Comment</div>
            <div class="tcolumn tcolumn3">Date archived</div>
            <div class="tcolumn tcolumn4">Article URL</div>
            </div>
            <?php
            $i=0;
            while($row = mysqli_fetch_array($result)) {
            ?>
            <div class="trow">
            <div class="tcolumn"><?php echo $row["0"]; ?></div>
            <div class="tcolumn"><?php echo $row["3"]; ?></div>
            <div class="tcolumn"><?php echo $row["2"]; ?></div>
            <div class="tcolumn"><?php echo $row["1"]; ?></div>
            </div>
            <?php
            $i++;
            }
            ?>
            <?php
            }
            else{
            echo "No result found";
            }




}
        function getallurl() {
            include 'db.php';
            $Bselect = "SELECT * FROM comments where id like $urlID";
            $resulturl = mysqli_query($conn,$Bselect);
            if (mysqli_num_rows($resulturl) > 0) {
            ?>
            <div class="div-table">
            <div class="trow">
            <div class="tcolumn tcolumn1">ID</div>
            <div class="tcolumn tcolumn2">Comment</div>
            <div class="tcolumn tcolumn3">Date archived</div>
            <div class="tcolumn tcolumn4">Article URL</div>
            </div>
            <?php
            $i=0;
            while($row1 = mysqli_fetch_array($resulturl)) {
            ?>
            <div class="trow">
            <div class="tcolumn"><?php echo $row1["0"]; ?></div>
            <div class="tcolumn"><?php echo $row1["3"]; ?></div>
            <div class="tcolumn"><?php echo $row1["2"]; ?></div>
            <div class="tcolumn"><?php echo $row1["1"]; ?></div>
            </div>
            <?php
            $i++;

            }
            ?>
            <?php
            }
            else{
            echo "No result found";
            }

}
        function thousandcomments() {
            include_once 'db.php';
            $result = mysqli_query($conn,"SELECT * FROM comments order by rand() limit 100");
            if (mysqli_num_rows($result) > 0) {
            ?>
            <div class="div-table">
            <div class="trow">
            <div class="tcolumn tcolumn1">ID</div>
            <div class="tcolumn tcolumn2">Comment</div>
            <div class="tcolumn tcolumn3">Date archived</div>
            <div class="tcolumn tcolumn4">Article URL</div>
            </div>
            <?php
            $i=0;
            while($row = mysqli_fetch_array($result)) {
            ?>
            <div class="trow">
            <div class="tcolumn"><?php echo $row["0"]; ?></div>
            <div class="tcolumn"><?php echo $row["3"]; ?></div>
            <div class="tcolumn"><?php echo $row["2"]; ?></div>
            <div class="tcolumn"><?php echo $row["1"]; ?></div>
            </div>
            <?php
            $i++;
            }
            ?>
            <?php
            }
            else{
            echo "No result found";
            }
}
?>


<?php
       function search1() {
            $search_value=$_POST["search"];
            include_once 'db.php';
            $result = mysqli_query($conn,"select * from comments where id like '%$search_value%' OR comment like '%$search_value%' OR dateimported like '%$search_value%' OR url like '%$search_value%'");
            if (mysqli_num_rows($result) > 0) {
            ?>
            <div class="div-table">
            <div class="trow">
            <div class="tcolumn tcolumn1">ID</div>
            <div class="tcolumn tcolumn2">Comment</div>
            <div class="tcolumn tcolumn3">Date archived</div>
            <div class="tcolumn tcolumn4">Article URL</div>
            </div>
            <?php
            $i=0;
            while($row = mysqli_fetch_array($result)) {
            ?>
            <div class="trow">
            <div class="tcolumn"><?php echo $row["0"]; ?></div>
            <div class="tcolumn"><?php echo $row["3"]; ?></div>
            <div class="tcolumn"><?php echo $row["2"]; ?></div>
            <div class="tcolumn"><?php echo $row["1"]; ?></div>
            </div>
            <?php
            $i++;
            }
            ?>
            <?php
            }
            else{
            echo "No result found";
            }

            }
?>

</div></div></div></div></body></html>

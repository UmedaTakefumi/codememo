<?php

function RandScatterPlot()
{

  $count_value_one=0;

  for ($loop_count=1; $loop_count<=100; $loop_count++) {

    $rand_num = mt_rand(1, 100);
    echo "$loop_count : $rand_num\n";  
    if ($rand_num==1) {
      $count_value_one++;
    }
  }  

}

RandScatterPlot();

?>

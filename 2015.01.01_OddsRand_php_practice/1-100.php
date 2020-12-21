<?php

$count_value_one=0;

echo "乱数生成アルゴリズムと確率の確認\n";


  for ($loop_count=1; $loop_count<=100; $loop_count++) {

    $rand_num = mt_rand(1, 100);
    echo "$loop_count : $rand_num\n";  
    if ($rand_num==1) {
      $count_value_one++;
    }
  }  

echo "1が生成された回数:$count_value_one\n"

?>

<?php

$output = [];
$return_var = '';
//echo exec('./mm_licenses_c 123456 0001', $output, $return_var);
echo exec('./gen.py F2CB56 0831', $output, $return_var);
echo exec('./gen.py', $output, $return_var);
$getAnswer = exec('./gen.py', $output, $return_var);
$getAnswer1 = exec('./gen.py 2342312', $output, $return_var);
$getAnswer2 = exec('./gen.py 234231', $output, $return_var);
$getAnswer3 = exec('./gen.py A2CB5S6 1001', $output, $return_var);
$getAnswer4 = exec('./gen.py A2CB56 10S01', $output, $return_var);
$getAnswer5 = exec('./gen.py A2CB56 1001', $output, $return_var);
$getAnswer6 = exec('./gen.py A2CB56 1001 rstr rstr', $output, $return_var);

print_r($output);
var_dump($return_var);



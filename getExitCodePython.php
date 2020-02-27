<?php

$output = [];
$return_var = '';
//echo exec('./mm_licenses_c 123456 0001', $output, $return_var);
echo exec('./gen.py', $output, $return_var);

$getAnswer01 = exec('./gen.py rst', $output, $return_var);
$getAnswer02 = exec('./gen.py A2CB56 0001', $output, $return_var);
$getAnswer03 = exec('./gen.py rst rsars nhdnd', $output, $return_var);

print_r($output);
var_dump($return_var);



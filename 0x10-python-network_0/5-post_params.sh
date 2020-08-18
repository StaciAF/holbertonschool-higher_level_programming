#!/bin/bash
# this script sends POST req displays the body of response passing POST variable
curl -s --data "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"

#!/bin/sh
TEST_FILES_BASE_URL='https://raw.github.com/Prill/puppet-sample-code/master/tests'
mkdir -p results
for testfile in exactmatch inexactmatch nomatch
    do
    python geturl.py $TEST_FILES_BASE_URL/$testfile results/$testfile-out
done

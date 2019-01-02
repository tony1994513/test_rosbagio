#!/bin/bash

for duration in 10 20 30 40; do
    for chunksize in 768 1024 5120 10240 20480 51200; do
        echo "excute duration: ${duration}"
        echo "excute chunksize: ${chunksize}"
        ./start_process.sh ${duration} ${chunksize}
    done
done


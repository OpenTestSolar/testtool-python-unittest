#! /bin/bash

set -exu -o pipefail

if [ -n "$TESTSOLAR_TTP_CLEANUP_CMDLINE" ]; then
    echo "Executing node cleanup command: $TESTSOLAR_TTP_CLEANUP_CMDLINE"
    eval "$TESTSOLAR_TTP_CLEANUP_CMDLINE"
fi
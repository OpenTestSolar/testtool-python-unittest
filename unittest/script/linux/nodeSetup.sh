#! /bin/bash

set -exu -o pipefail

if [ -n "$TESTSOLAR_TTP_SETUP_CMDLINE" ]; then
    echo "Executing node setup command: $TESTSOLAR_TTP_SETUP_CMDLINE"
    eval "$TESTSOLAR_TTP_SETUP_CMDLINE"
fi
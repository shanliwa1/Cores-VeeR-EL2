# Copyright (c) 2023 Antmicro <www.antmicro.com>
# SPDX-License-Identifier: Apache-2.0

import pyuvm
from cocotb.queue import QueueFull
from coordinator_seq import TestReadChannelSeq
from testbench import BaseTest

# FIXME       : This test is expected to fail.
# See description in `test_axi.py`


@pyuvm.test(expect_error=QueueFull)
class TestAXIReadChannel(BaseTest):
    def end_of_elaboration_phase(self):
        self.seq = TestReadChannelSeq.create("stimulus")

    async def run(self):
        self.raise_objection()
        await self.seq.start()
        self.drop_objection()

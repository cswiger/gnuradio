#!/usr/bin/env python
#
# Copyright 2014 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# GNU Radio is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# GNU Radio is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GNU Radio; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
#

from gnuradio import gr, gr_unittest
import fec_swig as fec
from _qa_helper import _qa_helper

from extended_encoder import extended_encoder
from extended_decoder import extended_decoder

class test_fecapi_dummy(gr_unittest.TestCase):

    def setUp(self):
        self.tb = gr.top_block()

    def tearDown(self):
        self.tb = None

    def test_parallelism0_00(self):
        frame_size = 30
        enc = fec.dummy_encoder_make(frame_size*8)
        dec = fec.dummy_decoder.make(frame_size*8)
        threading = None
        self.test = _qa_helper(10*frame_size, enc, dec, threading)
        self.tb.connect(self.test)
        self.tb.run()

        data_in = self.test.snk_input.data()
        data_out =self.test.snk_output.data()

        self.assertEqual(data_in, data_out)

    def test_parallelism0_01(self):
        frame_size = 30
        enc = fec.dummy_encoder_make(frame_size*8)
        dec = fec.dummy_decoder.make(frame_size*8)
        threading = 'ordinary'
        self.test = _qa_helper(10*frame_size, enc, dec, threading)
        self.tb.connect(self.test)
        self.tb.run()

        data_in = self.test.snk_input.data()
        data_out =self.test.snk_output.data()

        self.assertEqual(data_in, data_out)

    def test_parallelism0_02(self):
        frame_size = 30
        enc = fec.dummy_encoder_make(frame_size*8)
        dec = fec.dummy_decoder.make(frame_size*8)
        threading = 'capillary'
        self.test = _qa_helper(10*frame_size, enc, dec, threading)
        self.tb.connect(self.test)
        self.tb.run()

        data_in = self.test.snk_input.data()
        data_out =self.test.snk_output.data()

        self.assertEqual(data_in, data_out)

    def test_parallelism1_00(self):
        frame_size = 30
        enc = map((lambda a: fec.dummy_encoder_make(frame_size*8)), range(0,1))
        dec = map((lambda a: fec.dummy_decoder.make(frame_size*8)), range(0,1))
        threading = None
        self.test = _qa_helper(10*frame_size, enc, dec, threading)
        self.tb.connect(self.test)
        self.tb.run()

        data_in = self.test.snk_input.data()
        data_out =self.test.snk_output.data()

        self.assertEqual(data_in, data_out)

    def test_parallelism1_01(self):
        frame_size = 30
        enc = map((lambda a: fec.dummy_encoder_make(frame_size*8)), range(0,1))
        dec = map((lambda a: fec.dummy_decoder.make(frame_size*8)), range(0,1))
        threading = 'ordinary'
        self.test = _qa_helper(10*frame_size, enc, dec, threading)
        self.tb.connect(self.test)
        self.tb.run()

        data_in = self.test.snk_input.data()
        data_out =self.test.snk_output.data()

        self.assertEqual(data_in, data_out)

    def test_parallelism1_02(self):
        frame_size = 300
        enc = map((lambda a: fec.dummy_encoder_make(frame_size*8)), range(0,1))
        dec = map((lambda a: fec.dummy_decoder.make(frame_size*8)), range(0,1))
        threading = 'capillary'
        self.test = _qa_helper(10*frame_size, enc, dec, threading)
        self.tb.connect(self.test)
        self.tb.run()

        data_in = self.test.snk_input.data()
        data_out =self.test.snk_output.data()

        self.assertEqual(data_in, data_out)

    def test_parallelism1_03(self):
        frame_size = 30
        dims = 10
        enc = map((lambda a: fec.dummy_encoder_make(frame_size*8)), range(0,dims))
        dec = map((lambda a: fec.dummy_decoder.make(frame_size*8)), range(0,dims))
        threading = 'ordinary'
        self.test = _qa_helper(dims*frame_size, enc, dec, threading)
        self.tb.connect(self.test)
        self.tb.run()

        data_in = self.test.snk_input.data()
        data_out =self.test.snk_output.data()

        self.assertEqual(data_in, data_out)

    def test_parallelism1_04(self):
        frame_size = 30
        dims = 16
        enc = map((lambda a: fec.dummy_encoder_make(frame_size*8)), range(0,dims))
        dec = map((lambda a: fec.dummy_decoder.make(frame_size*8)), range(0,dims))
        threading = 'capillary'
        self.test = _qa_helper(dims*frame_size, enc, dec, threading)
        self.tb.connect(self.test)
        self.tb.run()

        data_in = self.test.snk_input.data()
        data_out =self.test.snk_output.data()

        self.assertEqual(data_in, data_out)

    def test_parallelism1_05(self):
        frame_size = 30
        dims = 5
        enc = map((lambda a: fec.dummy_encoder_make(frame_size*8)), range(0,dims))
        #dec = map((lambda a: fec.dummy_decoder.make(frame_size*8)), range(0,dims))
        threading = 'capillary'

        self.assertRaises(AttributeError, lambda: extended_encoder(enc, threading=threading, puncpat="11"))

    def test_parallelism1_06(self):
        frame_size = 30
        dims = 5
        #enc = map((lambda a: fec.dummy_encoder_make(frame_size*8)), range(0,dims))
        dec = map((lambda a: fec.dummy_decoder.make(frame_size*8)), range(0,dims))
        threading = 'capillary'

        self.assertRaises(AttributeError, lambda: extended_decoder(dec, threading=threading, puncpat="11"))

    def test_parallelism2_00(self):
        frame_size = 30
        dims1 = 16
        dims2 = 16
        enc = map((lambda b: map((lambda a: fec.dummy_encoder_make(frame_size*8)), range(0,dims1))), range(0,dims2))
        #dec = map((lambda b: map((lambda a: fec.dummy_decoder_make(frame_size*8)), range(0,dims1))), range(0,dims2))
        threading = 'capillary'

        self.assertRaises(AttributeError, lambda: extended_encoder(enc, threading=threading, puncpat="11"))

    def test_parallelism2_01(self):
        frame_size = 30
        dims1 = 16
        dims2 = 16
        dec = map((lambda b: map((lambda a: fec.dummy_decoder_make(frame_size*8)), range(0,dims1))), range(0,dims2))
        threading = 'capillary'

        self.assertRaises(AttributeError, lambda: extended_decoder(dec, threading=threading, puncpat="11"))

if __name__ == '__main__':
    gr_unittest.run(test_fecapi_dummy, "test_fecapi_dummy.xml")

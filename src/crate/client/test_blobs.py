from crate import client
from crate.client.exceptions import InvalidDigestException
from unittest import TestCase


class BlobContainerTest(TestCase):

    def test_get_none(self):
        conn = client.connect()
        blobs = conn.get_blob_container('dummy')
        self.assertRaises(InvalidDigestException, blobs.get, None)

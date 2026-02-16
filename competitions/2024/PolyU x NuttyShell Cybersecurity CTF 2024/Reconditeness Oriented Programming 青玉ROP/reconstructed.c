#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
  char *buf = malloc(52);
  srand(464);
  puts("?");
  gets_s(buf, 52);
  for (int times = 0; times < 100; ++times)
  {
    int idx1 = rand();
    int idx2 = rand();
    char old = buf[idx1 % 52];
    buf[idx1 % 52] = buf[idx2 % 52];
    buf[idx2 % 52] = old ^ rand();
  }
  if (!strncmp(buf,
               "\x6e\x05\xdf\xa1\xc6\x35\x34\x74\x3f\x92\x68\x36\xb6\x58\x42"
               "\x33\x7b\xea\x6f\xd6\xf8\x7e\x9f\xcc\xa3\xbf\x02\xd3\xf0\xf9"
               "\xa4\x22\x5f\xc0\xfa\x00\x01\x00\x65\x37\x10\xf5\xd7\xd1\xb9"
               "\x85\x8c\xbc\x6e\x20\x70\x57",
               52))
  {
    puts(":)");
    return 0;
  }
  return -1;
}

// PUCTF24{r0p_1n_r3v_e43183c9a5db551147ce7ac5dee5fbda}
// https://godbolt.org/#z:OYLghAFBqd5QCxAYwPYBMCmBRdBLAF1QCcAaPECAMzwBtMA7AQwFtMQByARg9KtQYEAysib0QXACx8BBAKoBnTAAUAHpwAMvAFYTStJg1AB9U8lJL6yAngGVG6AMKpaAVxYM9DgDJ4GmADl3ACNMYhAAJgAOUgAHVAVCWwZnNw89eMSbAV9/IJZQ8OiLTCtshiECJmICVPdPLhKy5MrqglzAkLDImIUqmrr0xr62jvzCnoBKC1RXYmR2DgBSCIBmP2Q3LABqJdXHPvxUADoEPewljQBBFfWGTdcdvYOCdFo8YNPzy5u1ja3MLt9n1iH5gF9Vhdrj8/ARtiwmH4IJNdgB2ABCP222O2yAQ1W2ACpgq4qECACLwsS0VDICAAVgikz2mOuOO2CmIhnQEEkADZJMzVqyruzYq4CAoICsInsAGIyoUi9nETBMHkaUjbElULWMpVYnH8YjbCCw7Y2NgKCnbDQsi14K1AxzbLgaO3C3YRTHey2YBQopYYw3s7HmvDoVRcG1chg8g1s0NhwTbCOqCIx7nIlkh0N4gkudA2nVLenotPRlb07aM0vknOJpMlssVr3V2v0yl7SnN8uRjNVmuyzsN0VJ7Wk0t99Ntod1m2F3b07DbWPx0fsoP1xupskQMBgEH3FixCA60i58dJmWlxyqPmYW%2BqDT0p/oKhPphcJ/IPlP1avvSd6rJIT6oqBQGqKsH6QQAnMOd58lE/5/pBwSoXe9LIZBkiyhEso7leoY3pBqyrGBwRPmqT58jBd7oBhqhUNhd6oo%2BcF0aoyDIJ%2B5FoZxGgIao6B8XeVB2pBVCwTehFETiJF3kwEF3vhT70pxyASWJTBPu6unfpBemQXygHAaiT5uk%2BVCmcJ5mQegBl3sE0mqbJclekJUQ2VEPFob5iHsSpWmqKiwX0uZ%2BEXm5cn6oGwbReKkrSvhIDMvhCZjkmqoEHMDC2hu8motumWrpgOXEHlAC037Cj8W4/Bw0y0Jw9K8J4HBaKQqCcC6CizPMgK3DwpAEJojXTAA1iA9Kas1HCSG1Y1dZwvAKCAmqjR1jWkHAsAwIgKCoCedBhOQlBoMd9DhMgwBcKsER8HQBBhGtZ5LcEfjVAAnpww0fcwxBfQA8sE2iYNYv28BdbCCEDDC0D9W2kFgJLAI41JrdwvBYAiRjiEj%2BCqtYeAAG7%2BktmCqODEqLMNsKlEt7zBFygPOFgS0EKCLCQ9MVAGMACgAGp4JgADuQOxIwkMyIIIhiOwUgy/IShqEtuiNAYRggKYxjmEza2QNMqCxOUmOVYc3bIFww2oGTxCglgBvIk04PlPYcaDA0pA%2BH4nQFN0jSZEkAiexkCTBwwYxdOEwylK7LT9LULj1HoljxwIrQ1FH/sxxYieh8MifZxMXDTH1cwLBITUtYtSPdRw2yqFEfKVQK2zANxrqrMcGYQLghAkF6qyl7wm1aJMk3TbNnALaQ3MzaQ7WdfXq3rSNY3TLtB2U9TRBkBQEDVALyiGKUQgIKgovtcNF2xHQTDlCf/i0Ofl9L1DR131dKC3fdpC3ydYgARWCLA/pdMIQMJSvyvhTKmyArjEAFitb2cDKj4E8MoOQjgAAqcoIigQxMQDQsRjBcAYMYYgqwSbGEwJIYeURVjIFgkwek6Bgj0npNbSQqIFioiYMgVhmBMDqWCOgHSRUlZy3EIrfgghFAqHUEjdW%2BhDAmDMPoD4TsjYm2SGbC2qxyRWxtnbB25NDakGIK4QQjpMDYNQC4LRMwK4Kzzugp%2BZ8L4wKRpzIRa9RZcliDzfQNdF5LXrtgOBEpB5Nxbm3DuyAu491NI4LU/c95DxHuvLaE9gnzV4PPTU79locFXhtDek8F5zVWLXZeyCx7jVyREGpvAV5ZPHtMO2iQ7CSCAA%3D

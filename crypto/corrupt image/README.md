# Corrupted file

In this challenge contestants will have to decrypt a file using the gpg keys provided. The private key is obviously password protected, the original challenge had the password "a".
In retesting for the demo something went wrong and I recreated the files again. 

## Solution

```bash
> gpg2john private.gpg > key
> john key
-- result --
ctf@challenge.pt:**Challengectf**:::ctf@challenge.pt <ctf@challenge.pt>::private.pgp

> gpg --import private.gpg
> gpg -e challenge.gpg
```

## Flag 

ctf{s4f3_gpg_3ncrpyt3d_f1l3}



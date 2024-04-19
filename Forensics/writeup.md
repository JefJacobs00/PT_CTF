# Challenge

git get got [Easy]

## Description

My friend has sent me his secret cat stash. Can you figure out why he is so secretive about this?

## Solutions
There is a .git folder where if you check the diff with the first one you can see that the flag is renamed to the hash of the image.

```bash
commit b588d30aafc35d1cac65d6fc5ff92dcad9f04626 (HEAD -> main, origin/main)
Author: Jef Jacobs <2345@ilias-solutions.com>
Date:   Thu Apr 11 17:13:11 2024 +0200

    removed not cute cats

commit 124b6aed8cf7d42b8e7a5196b80dc7108d9f1dc1
Author: Jef Jacobs <2345@ilias-solutions.com>
Date:   Thu Apr 11 17:12:56 2024 +0200

    removed script

commit 4ccb333ba85adfc251df58893086171178532564
Author: Jef Jacobs <2345@ilias-solutions.com>
Date:   Thu Apr 11 17:12:38 2024 +0200

    rename pictures

commit fdbcdd4ea36d30705430fdbd82e084092b005ef2
Author: Jef Jacobs <2345@ilias-solutions.com>
Date:   Thu Apr 11 17:11:10 2024 +0200

initial

$ git show fdbcdd4ea36d30705430fdbd82e084092b005ef2

...
index 0000000..df8995a
Binary files /dev/null and b/ctf{cats_are_t0_cute_to_n0t_h4v3_a_picture_stash}.jpeg differ
diff --git a/download.jpeg b/download.jpeg
new file mode 100644
index 0000000..46b368a
...
```

## flag 
ctf{cats_are_t0_cute_to_n0t_h4v3_a_picture_stash}.jpeg

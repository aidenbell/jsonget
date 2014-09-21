# JSONGet

JSONGet is a really simple tool for configuring command-line programs from JSON configuration files. The idea is that you can extract values from JSON files to form command-line arguments for your server or program. The arguments passed to JSONGet then form values suitable for passing to `xargs` or something.

## Example

Here's an example of getting JSON values and associating them with arguments

```
]$ jsonget.py myconfig.json -hostname config[0].hostname -port config[0].port
-hostname "host1.example.com"
-port "8080"
```
  
Passing the output to `xargs` allows you to run your program with those flags.

```
]$ jsonget.py myconfig.json -hostname config[0].hostname -port config[0].port | xargs myserver
```

This is useful for shell scripting, daemon startup scripts and other things. 

## Current state

Initial commit, just a script I hacked together in 10 minutes to quickly store configurations and extract them in to command-line arguments. Might improve validation, exception handling and tests if I use it often or others find it useful. Just a little script, might as well make it public.

## License

See license file in repo.

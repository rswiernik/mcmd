# mcmd Documentation

The general workflow for the daemon process goes something like this:
- Spawn daemon process
  - Set up logging and other niceties
- Detect if servers that we previously set up are running on the system
  - Recreate the objects that the daemon would need
    - Possibly just pickle them and unpickle when needed
- Open Unix socket
- Restrict socket write to minecraftadmins Unix group
  - Possibility of having this be able to be set by the user
- cmd: create
  - create empty object for server
    - Spawn server process and allow basic files to be created
    - Read in all of the config information
- cmd: start [server name]
  - check to see if there is already a server with that name
  - if not make it
- cmd: stop [server name]
  - stop the requested server
- cmd: restart
- cmd: list
- cmd: server-mod
  - mod info about the server

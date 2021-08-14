<h1 align="center">
  Pwnagotchi Community Plugins
</h1>

<p align="center">
  <a style="text-decoration:none" href="https://www.python.org/downloads/release/python-379/">
    <img src="https://img.shields.io/badge/python-3.7+-blue.svg?color=00B16A&style=flat-square" alt="Python Version" />
  </a>
  <a style="text-decoration:none">
    <img src="https://img.shields.io/badge/OS-Linux-blue?style=flat-square&color=00B16A" alt="OS" />
  </a>
</p>

This is a third-party unofficial plugin repository for [Pwnagotchi](https://github.com/evilsocket/pwnagotchi). **Use the plugins at your own risk**.

<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#downloading">Downloading</a>
      <ul>
        <li><a href="#using-git-clone">Using Git Clone</a></li>
        <li><a href="#using-pwnagotchi-plugin-manager">Using Pwnagotchi Plugin Manager</a></li>
      </ul>
    </li>
    <li>
      <a href="#enabling">Enabling</a>
      <ul>
        <li><a href="#from-config-file">From Config File</a></li>
        <li><a href="#from-pwnagotchi-plugin-manager">From Pwnagotchi Plugin Manager</a></li>
      </ul>
    </li>
    <li><a href="#configuration">Configuration</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>


## Downloading

### Using Git Clone:

In order to use these plugins, clone the repository anywhere on your unit:

```shell
cd /path/to/plugin/directory

git clone https://github.com/Teraskull/pwnagotchi-community-plugins/
```

Add the absolute path to `/etc/pwnagotchi/config.toml`:

```toml
main.custom_plugins = "/path/to/plugin/directory"
```

> By default, `/usr/local/share/pwnagotchi/installed-plugins/` is used.


### Using Pwnagotchi Plugin Manager:

Another way to install plugins is to add the repo to `/etc/pwnagotchi/config.toml`:

```toml
main.custom_plugin_repos = [
  "https://github.com/evilsocket/pwnagotchi-plugins-contrib/archive/master.zip",
  "https://github.com/Teraskull/pwnagotchi-community-plugins/archive/master.zip"
]
```

Then you can use the Pwnagotchi plugin manager to install the plugins:

```shell
sudo pwnagotchi plugins update

sudo pwnagotchi plugins list

sudo pwnagotchi plugins install plugin_name
```


## Enabling

### From Config File:

To enable a previously downloaded plugin, add the following line to `/etc/pwnagotchi/config.toml`:

```toml
main.plugins.plugin_name.enabled = true
```

Where `plugin_name` is the filename of the plugin.


### From Pwnagotchi Plugin Manager:

If you are using the Pwnagotchi plugin manager, enable plugins with the following command:

```shell
sudo pwnagotchi plugins enable plugin_name
```


## Configuration

If a plugin has additional configuration options, add them as per the `.toml` file for the corresponding plugin.

For example, here is how to enable the `Clock` plugin and set configuration options for it in `/etc/pwnagotchi/config.toml`:
```toml
main.plugins.clock.enabled = true

main.plugins.clock.date_format = "%d/%m/%y"
main.plugins.clock.time_format = "%H:%M"
```


## Contributing

If you would like to add a plugin to this repository, open a PR which includes:

1. The Python plugin file, named in `snake_case.py`.
2. The `.toml` file with all possible configurations for the plugin, if they exist. Filename should be the same as the plugin name.
3. A screenshot of the display web interface to see how the plugin looks like.
4. Brief description of the plugin.
5. What displays the plugin was tested on.
6. Does the plugin interfere with other official/third-party plugins (For example, the text is layered on top of existing text).

> These guidelines make sure that the plugin list is consistent.


## License

The community-created plugins are released under the `GPL3` license.

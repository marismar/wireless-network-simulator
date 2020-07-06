<h1 align="center">Wireless Network Simulator 📡</h1>


<h4 align="center">
  A wireless network simulator developed in python, as a final project of the wireless networks course at UFPB.
</h4>

<p align="center">
  <a href="https://www.overleaf.com/project/5e87ee38b01f50000176e3e6" target="_blank">
    <img alt="Documentation" src="https://img.shields.io/badge/documentation-yes-brightgreen.svg" />
  </a>
  <a href="https://github.com/marismarcosta/wireless-network/blob/master/LICENSE" target="_blank">
    <img alt="license: MIT" src="https://img.shields.io/badge/license-MIT-brightgreen.svg" />
  </a>
</p>

<p align="center">
  <a href="#workflow">Workflow</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#layers">Layers</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#setup">Setup</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#run">Run</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#license">License</a>
</p>

## Table of Contents

* [Layers Description](#layers-description)

* [Input setup](#input-setup)
  * [Creating a host](#creating-a-host)
  * [Creating a data package](#creating-a-data-package)

* [Run tests](#run-tests)

* [Authors](#authors)


## Workflow

## Layers

Write some description

### Phisical

### Link

### Network


## Setup
 
### Creating a host

Create a host by wirting ` new_host = host(host_id, x_position, y_position, master, range_ratio) ` into the main.js. The **master** <br> is the entity that decides which host will send data, so you must create only one master. 

### Creating a data package

Create a data package for any host by : `host_name.send_message("message content", receiver_host_id)`


## Run

Go into the file project then open the terminal and write the command bellow :

```
python main.py
```

## Authors

👤 **Marismar da Costa Silva**

* Github: [@marismarcosta](https://github.com/marismarcosta)
* LinkedIn: [@marismarcosta](https://linkedin.com/in/marismarcosta)

👤 **Gustavo Eraldo da Silva**

* Github: [@EraldoCi](https://github.com/EraldoCi)
* LinkedIn: [@gustavoeraldo](https://linkedin.com/in/gustavoeraldo)

## Show your support

Give a ⭐️ if this project helped you!

## License

Copyright © 2020 [Marismar da Costa Silva](https://github.com/marismarcosta), [Gustavo Eraldo da Silva](https://github.com/EraldoCi).<br />
This project is [MIT](https://github.com/marismarcosta/wireless-network/blob/master/LICENSE) licensed.

*****
###### This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)

# Repositorio de github

Git es un software de control de versiones y es la manera principal en la que se desarrolla y comparte código. Lo inventó Linus Torvalds, el creador de Linux, para diseñar sus sistemas operativos.

## El README.md

Este documento se llama README, su extensión es `.md` y lo usamos para explicar los contenidos de nuestro repositorio, usualmente contiene nociones básicas del módulo o librería y un pequeño instructivo de cómo se usa. El lenguaje en el que se escribe el README se llama _Markdown_ y permite formatear texto de manera básica o usando html e incluso LatEx (lenguaje para expresiones matemáticas).

## Las ramas

Una gran herramienta de este software es la posibilidad de crear ramas, para desarrollar sobre el mismo código en paralelo y luego manejar conflictos (en caso de que existan) al hacer el _merge_ de esas ramas a la rama principal (_main_). 

En este caso, creamos una rama para cada grupo de TP (los aprobados) y vamos a mergear a main las que correspondan en el caso de que tengan ganas de compartir lo que hicieron. Si no tienen ganas de exponer lo que armaron, eliminamos la rama y ese código ya no es accesible. 

## Los commits

Cada cambio que fuimos haciendo (y que queramos revertir) se guarda en un _commit_, que además tiene su propio mensaje para identificar en caso de necesitarlo. Es también una de las cosas más útiles de este software, imaginen que están trabajando en un documento y cada vez que guardan pueden identificar ese guardado de alguna manera.

## Comandos de git [avanzado]

Git es el lenguaje en el que se controlan los elementos ya mencionados. Cuando tenemos un repositorio en nuestro local y le hacemos una modificación, es posible llevar esa modificación al servidor (en este caso, un servidor de Github, existe también Gitlab) usando la interfaz o a través de comandos en la terminal (estando sobre el directorio local en el que está el repositorio):

- `git add .` : agrega los cambios 

- `git commit -m "mi mensaje de commit"` : lleva los cambios agregados a un área intermedia llamada "staging" y los etiqueta con el mensaje de commit

- `git push` : lleva los cambios al servidor

- `git checkout -b nueva/rama` : crea una nueva rama (llamada nueva/rama) localmente y se cambia para estar sobre esa rama


## Autenticación [avanzado]

Para clonar un repositorio (tenerlo en nuestro local), para _commitear_ cambios y para _pushearlos_, es necesario autenticar nuestro local en el servidor. Es decir, le tenemos que "decir a github" que nuestra compu se corresponde con nuestro usuario y que, por lo tanto, tiene los mismos accesos y permisos que tiene nuestro usuario. 

Esto se hace a través de distintos protocolos, la preferencia es personal pero el protocolo SSH es relativamente fácil de seguir: https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent.
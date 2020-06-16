# Bot para comentar curtir e seguir pessoas no instagram

Fazendo uso do selenium webdriver 

<p align="center">
  <img width="460" height="300" src="https://media1.tenor.com/images/f45126cde56eaf82e1f506cbdf65cec2/tenor.gif?itemid=14086631">
</p>



### Requisitos

Os requisitos são mínimos, uma máquina com 2gb de ram e poucas paginas abertas consegue executar com tranquilidade.

```
2gb ram -- processador intel inside ou paralelo ao mesmo -- sistema operacional windows -- vs code -- python3.7 ou superior
```

### Instalando

Para iniciar o projeto é necessario utilizar o VS code, já executei o projeto com o sublime text3 porém optei
por dar continuidade com o vs code para ser mais acessível a contribuições.

<p align="center">
  <img width="660" height="500" src="https://user-images.githubusercontent.com/66971579/84747369-88e24080-af8d-11ea-8bce-dea3e5400ddb.jpeg">
</p>

[instale o vs code clicanco aqui](https://code.visualstudio.com/Download)


## executando 0.1

Para iniciar o projeto é necessário o selenium, eu o instalei pelo cmd através do modulo pip simplesmente utilizando os comandos abaixo:

```
pip install selenium
```

## executando 0.2

Agora será necessário baixar o geckodriver, que é utilizado para acessar o navegador mozila firefox caso o navegador utilizado fosse
o chrome seria necessário baixar o chromedriver. 

[instale o gecodriver 64bits clicanco aqui](https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-win64.zip)

[instale o gecodriver 32bits clicanco aqui](https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-win32.zip)

## Importante ressaltar
Em algumas máquinas o geckodriver não é adicionado ao path, então é necessário adiciona-lo manualmente pelas variáveis de sistema.
sendo possível acessalas pela barra de pesquisa. Caso ache necessário modifique o caminho do codigo na classe "instagrambot" para ficar compatível ao de 
sua maquina.

<p align="center">
  <img width="660" height="500" src="https://user-images.githubusercontent.com/66971579/84749956-0b203400-af91-11ea-82a0-1e6c2ed7d87e.jpeg">
</p>


## executando 0.3
Adicione á hashtag de sua preferencia para que o bot possa pesquisar e curtir, o bot irá curtir,comentar e depois irá seguir os usuarios que 
seguem a hashtag, o campo para adicionar a hashtag esta selecionada na imagem abaixo:
<p align="center">
  <img width="660" height="500" src="https://user-images.githubusercontent.com/66971579/84751264-bed5f380-af92-11ea-9dea-97a98a79bb98.jpeg">
</p>

## executando 0.4

Por ultimo é necessário adicionar informações de login do seu usuário ao final do código:

<p align="center">
  <img width="660" height="500" src="https://user-images.githubusercontent.com/66971579/84751541-11171480-af93-11ea-921e-456c361649e4.jpeg">
</p>



### Considerações finais 

É importante se atentar as atualizações das tags e hrefs que o instagram utiliza, pois as mesmas podem ser modificadas sendo necessário 
consultar o codigo da pagina e se necessário substituir, outro ponto a se atentar é as atualizações dos navegadores e do webdriver.








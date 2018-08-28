# -*- coding: utf-8 -*-
# autor thewalking.miguel
# version 0.1.1

import os

from bs4 import BeautifulSoup

from urllib.request import FancyURLopener
from urllib.parse import urlencode


def descargarFuentes(destino, br, ORIGEN):
    if not os.path.exists(destino + "tpls/oficial/css/fonts/"):
        os.makedirs(destino + "tpls/oficial/css/fonts/")

    br.retrieve(ORIGEN + "tpls/oficial/css/fonts/OFLGoudyStM-webfont.ttf",
                destino + "tpls/oficial/css/fonts/OFLGoudyStM-webfont.ttf")
    br.retrieve(
        ORIGEN + "tpls/oficial/css/fonts/cardinal-alternate-webfont.woff",
        destino + "tpls/oficial/css/fonts/cardinal-alternate-webfont.woff")
    br.retrieve(
        ORIGEN + "tpls/oficial/css/fonts/cardinal-alternate-webfont.ttf",
        destino + "tpls/oficial/css/fonts/cardinal-alternate-webfont.ttf")


def descargaCss(soup, destino, br, ORIGEN):
    recursos = soup.find_all("link", {"type": "text/css"})

    for recurso in recursos:
        fichero = recurso.get("href")
        partes = fichero.split("/")
        prueba2 = partes[-1].split("?")[0]

        directorio_tmp = destino
        for parte in partes[1:-1]:
            directorio_tmp += parte + "/"

        if not os.path.exists(directorio_tmp):
            os.makedirs(directorio_tmp)

        br.retrieve(ORIGEN + recurso.get("href"), directorio_tmp + prueba2)


def descargaJs(soup, destino, br, ORIGEN):
    recursos = soup.find_all("script", {"type": "text/javascript"})

    for recurso in recursos:
        fichero = recurso.get("src")
        if not fichero is None:
            partes = fichero.split("/")
            prueba2 = partes[-1].split("?")[0]

            directorio_tmp = destino
            for parte in partes[1:-1]:
                directorio_tmp += parte + "/"

            if not os.path.exists(directorio_tmp):
                os.makedirs(directorio_tmp)
            br.retrieve(ORIGEN + recurso.get("src"), directorio_tmp + prueba2)


def imagenesPortada(soup, destino, br, ORIGEN, descargados):
    recursos = soup.find_all("img")
    for recurso in recursos:
        if ORIGEN + recurso.get("src") not in descargados:
            descargados[ORIGEN + recurso.get("src")] = recurso.get("src")
            fichero = recurso.get("src")
            partes = fichero.split("/")
            prueba2 = partes[-1]
            if partes[1] == "imgs" or partes[1] == "tpls":

                directorio_tmp = destino
                for parte in partes[1:-1]:
                    directorio_tmp += parte + "/"

                if not os.path.exists(directorio_tmp):
                    os.makedirs(directorio_tmp)
                br.retrieve(ORIGEN + recurso.get("src"),
                            directorio_tmp + prueba2)


def descargarEscenas(soup, destino, br, ORIGEN, descargados):
    recursos = soup.find_all("a", {"class": "tituloEscena"})
    for recurso in recursos:
        escena = ORIGEN + recurso.get("href")[1:]
        descargaEscena(soup, destino, br, ORIGEN, escena, descargados)


def descargaEscena(soup, destino, br, ORIGEN, link, descargados):
    escena = BeautifulSoup(br.open(link).read(), features="html5lib")
    fichero = escena.find("h3", {"id": "escena"}).text.replace(" ", "_")
    f = open(destino + fichero + ".html", "w")
    hay_siguiente = escena.find("a", {"title": u"Página siguiente"})

    if hay_siguiente:
        div_principal = escena.find_all("div", {"class": "wrapMensaje"})[-1]
        # encontrar el ultimo post de la primera
        while hay_siguiente:
            escena_tmp = BeautifulSoup(
                br.open(ORIGEN + hay_siguiente["href"]).read(),
                features="html5lib")

            posts = escena_tmp.find_all("div", {"class": "wrapMensaje"})
            # insert posts en el form nombre_div
            for post in posts:
                div_principal.insert_after(post)
                div_principal = post
            hay_siguiente = escena_tmp.find("a", {"title": u"Página siguiente"})

    limpiarEscena(escena, True)
    imagenesPortada(escena, destino, br, ORIGEN, descargados)
    f.write(escena.prettify())
    f.close()


def limpiarEscena(soup, es_escena):
    # Eliminar barra lateral y superior
    soup.find('div', id="cabecera").decompose()
    soup.find('div', id="navegador").decompose()

    # modifico links para que apunten a local
    portada = soup.find("h2", {"class": "tituloPartida"})
    portada.a["href"] = "./portada.html"

    escenas = soup.find("div", {"id": "listaEscenas"})
    for esc in escenas.find_all("li"):
        if esc.a.text == "Portada":
            esc.a["href"] = "./portada.html"
        else:
            esc.a["href"] = "./" + esc.a.text.replace(" ", "_") + ".html"

    ponerLinksLocal(soup)

    lista = ["linkdialogConfigurar", "linkdialogEscenas", "linkdialogVips"]
    for el in lista:
        dialogo = soup.find("a", {"id": el})
        if dialogo:
            dialogo.decompose()
    if es_escena:
        for ul in soup.find_all("ul", {"class": "paginador"}):
            ul.decompose()

    soup.find("a", {"id": "linkdialogJugadores"})[
        "href"] = "./menu_jugadores.html"
    soup.find_all("a", {"id": "linkdialogWrapper"})[0][
        "href"] = "./menu_personajes.html"

    if len(soup.find_all("a", {"id": "linkdialogWrapper"})) > 1:
        soup.find_all("a", {"id": "linkdialogWrapper"})[1][
            "href"] = "./menu_pnjs.html"


def ponerLinksLocal(soup):
    javascripts = soup.find_all("script", {"type": "text/javascript"})
    estilos = soup.find_all("link", {"type": "text/css"})
    imagenes = soup.find_all("img")

    for j in javascripts:
        fichero = j.get("src")
        if not fichero is None:
            j["src"] = "." + j.get("src")

    for e in estilos:
        e["href"] = "." + e.get("href")

    for i in imagenes:
        fichero = i.get("src")
        partes = fichero.split("/")
        if partes[1] == "imgs" or partes[1] == "tpls":
            i["src"] = "." + i.get("src")


def limpiarPortada(soup):
    ultimos = soup.find_all("div", {"class": "ultimo_mensaje"})
    herramientas = soup.find_all("div", {"class": "herramientas"})

    for u in ultimos:
        u.decompose()

    for h in herramientas:
        h.decompose()
    recursos = soup.find_all("a", {"class": "tituloEscena"})
    for escena in recursos:
        escena["href"] = "./" + escena.text.replace(" ", "_") + ".html"


def descargarJugadores(recursos, soup, destino, br, ORIGEN, descargados):
    f = open(destino + 'menu_jugadores.html', 'w')
    link = soup.find("a", {"id": "linkdialogJugadores"})

    pers = BeautifulSoup(br.open(ORIGEN + link["href"]).read(),
                         features="html5lib")

    if recursos:
        for css in recursos:
            css["href"] = css["href"][1:]
            pers.head.append(css)
    imagenesPortada(pers, destino, br, ORIGEN, descargados)
    ponerLinksLocal(pers)
    f.write(pers.prettify())
    f.close()


def descargarPersonajes(recursos, soup, destino, br, ORIGEN, descargados):
    f = open(destino + 'menu_personajes.html', 'w')
    link = soup.find_all("a", {"id": "linkdialogWrapper"})

    pers = BeautifulSoup(br.open(ORIGEN + link[0]["href"]).read(),
                         features="html5lib")

    if recursos:
        for css in recursos:
            css["href"] = css["href"][1:]
            pers.head.append(css)

    imagenesPortada(pers, destino, br, ORIGEN, descargados)
    ponerLinksLocal(pers)
    f.write(pers.prettify())
    f.close()


def descargarPNJs(recursos, soup, destino, br, ORIGEN, descargados):
    link = soup.find_all("a", {"id": "linkdialogWrapper"})
    if len(link) > 1:
        f = open(destino + 'menu_pnjs.html', 'w')
        pers = BeautifulSoup(br.open(ORIGEN + link[1]["href"]).read(),
                             features="html5lib")
        if recursos:
            for css in recursos:
                css["href"] = css["href"][1:]
                pers.head.append(css)

        imagenesPortada(pers, destino, br, ORIGEN, descargados)
        ponerLinksLocal(pers)
        f.write(pers.prettify())
        f.close()


def hayPaginadorPortada(soup, destino, br, ORIGEN, descargados):
    hay_siguiente = soup.find("a", {"title": u"Página siguiente"})
    ultima_escena = soup.find_all("div", {"class": "escena"})[-1]
    while hay_siguiente:
        portada_tmp = BeautifulSoup(
            br.open(ORIGEN + hay_siguiente["href"]).read(), features="html5lib")

        escenas = portada_tmp.find_all("div", {"class": "escena"})
        # insert posts en el form nombre_div
        for esc in escenas:
            ultima_escena.insert_after(esc)
            ultima_escena = esc

        hay_siguiente = portada_tmp.find("a", {"title": u"Página siguiente"})


def main():
    ORIGEN = "https://www.comunidadumbria.com/"
    try:
        from umbria.descargar_gui import main as main_qt
    except ImportError:
        usuario = input("Usuario:")
        password = input("Password:")
        slug = input(
            "Dirección de la partida: www.comunidadumbria.com/partida/")
        destino = input("Directorio de destino:")
    else:
        usuario, password, slug, destino = main_qt()

    if destino[-1] != "/":
        destino = destino + "/"

    abridor = FancyURLopener()
    abridor.open(ORIGEN)
    abridor.open(ORIGEN, bytes(
        urlencode({'ACCESO': usuario, 'CLAVE': password}), 'utf-8'))

    r = abridor.open(ORIGEN + "partida/" + slug).read()

    soup = BeautifulSoup(r, features="html5lib")
    copia_sopa = BeautifulSoup(r, features="html5lib")
    limpiarEscena(soup, False)
    descargados = {}

    hayPaginadorPortada(soup, destino, abridor, ORIGEN, descargados)
    descargarEscenas(soup, destino, abridor, ORIGEN, descargados)
    descargaCss(soup, destino, abridor, ORIGEN)
    descargaJs(soup, destino, abridor, ORIGEN)
    imagenesPortada(soup, destino, abridor, ORIGEN, descargados)
    # descargar imagenes de portada

    recursos = copia_sopa.find_all("link", {"type": "text/css"})
    descargarPersonajes(recursos, copia_sopa, destino, abridor, ORIGEN, descargados)
    descargarJugadores(recursos, copia_sopa, destino, abridor, ORIGEN, descargados)
    descargarPNJs(recursos, copia_sopa, destino, abridor, ORIGEN, descargados)
    descargarFuentes(destino, abridor, ORIGEN)
    limpiarPortada(soup)

    f = open(destino + 'portada.html', 'w')
    f.write(soup.prettify())
    f.close()


if __name__ == "__main__":
    main()

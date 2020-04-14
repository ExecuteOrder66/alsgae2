#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import factura
from datetime import datetime
from webapp2_extras import jinja2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

    def post(self):
        cif = self.request.get("cif")
        nombre = self.request.get("nombre")
        direccion = self.request.get("direccion")
        poblacion = self.request.get("poblacion")
        provincia = self.request.get("provincia")
        codigo_postal = self.request.get("codigopostal", 0)
        pais = self.request.get("pais")
        persona_de_contacto = self.request.get("personadecontacto")
        email = self.request.get("email")
        telefono = self.request.get("telefono")

        concepto = self.request.get("concepto")
        precio = self.request.get("precio", 0)
        unidades = self.request.get("unidades", 0)
        importe_bruto = 0
        iva = self.request.get("iva", 0)
        importe_total = 0

        if (cif is None) or (nombre is None) or (direccion is None) or (poblacion is None) or (codigo_postal is None) \
                or (pais is None) or (persona_de_contacto is None) or (email is None) or (telefono is None) or (
                concepto is None) or (provincia is None)\
                or (precio is None) or (unidades is None):
            self.response.write("No se pueden procesar datos vacios")
        else:
            if precio.isdigit() and unidades.isdigit() and iva.isdigit():
                importe_bruto = int(precio) * int(unidades)
                importe_total = importe_bruto * ((100 + int(iva)) / 100)
            else:
                self.response.write("Debe introducir numeros en los campos precio, unidades e iva")

        fecha = datetime.now()
        linea = factura.LineaDeDetalle(concepto, precio, unidades, importe_bruto, iva, importe_total)

        jinja = jinja2.get_jinja2(app=self.app)
        valores = {
            "cif": cif,
            "nombre": nombre,
            "direccion": direccion,
            "poblacion": poblacion,
            "provincia": provincia,
            "codigopostal": codigo_postal,
            "pais": pais,
            "personadecontacto": persona_de_contacto,
            "email": email,
            "telefono": telefono,
            "linea": linea,
            "importebruto": importe_bruto,
            "importetotal": importe_total,
            "fecha": fecha
        }

        self.response.write(jinja.render_template("answer.html", **valores))


app = webapp2.WSGIApplication([
    ('/factura', MainHandler)
], debug=True)

<!-- eslint-disable -->
<template>
  <div class="jumbotron vertical-center">
    <div class="container">
      <!--Bootswatch CDN  -->
      <link
        rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/litera/bootstrap.min.css"
        integrity="sha384-enpDwFISL6M3ZGZ50Tjo8m65q06uLVnyvkFO3rsoW0UC15ATBFz3QEhr3hmxpYsn"
        crossorigin="anonymous"
      />
      <link
        rel="stylesheet"
        href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-icons/1.11.3/font/bootstrap-icons.min.css"
      />
      <div class="row">
        <div class="col-sm-12" style="font-size: 25px">
          <p>Repositorio de Carros</p>
          <hr />
          <br />
          <!--Alert Message-->
          <button
            type="button"
            class="btn btn-success btn-sm bi bi-plus-square-dotted"
            style="font-size: 12px"
          >
            Añadir nuevo vehículo
          </button>

          <br /><br />
          <table class="table table-hover">
            <!--Table Head -->
            <thead>
              <tr>
                <!-- Table Header Cells -->
                <th scope="col">Marca</th>
                <th scope="col">Modelo</th>
                <th scope="col">Placa</th>
                <th scope="col">Color</th>
                <th scope="col">Tipo de Vehículo</th>
                <th scope="col">Propietario</th>
                <th scope="col">Teléfono</th>
                <th scope="col">Correo</th>
                <th scope="col">Acciones</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Hyndai</td>
                <td>I10</td>
                <td>PGB-8932</td>
                <td>Tomate</td>
                <td>Sedán</td>
                <td>Carlos Vaca</td>
                <td>09999</td>
                <td>09999</td>
                <td>
                  <div class="btn-group" role="group">
                    <button type="button" class="btn btn-info">Actualizar</button>
                    <button type="button" class="btn btn-danger">Eliminar</button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

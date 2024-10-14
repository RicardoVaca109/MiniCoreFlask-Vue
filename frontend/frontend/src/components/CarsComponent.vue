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
          <h1 class="text-center bg-primary text-white" style="border-radius: 10px;">Repositorio de Carros</h1>
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
              <tr v-for="vehiculo in vehiculos" :key="vehiculo.id">
                <td>{{ vehiculo.marca }}</td>
                <td>{{ vehiculo.modelo }}</td>
                <td>{{ vehiculo.placa }}</td>
                <td>{{ vehiculo.color }}</td>
                <td>{{ vehiculo.tipo_vehiculo }}</td>
                <td>{{ vehiculo.propietario }}</td>
                <td>{{ vehiculo.telefono }}</td>
                <td>{{ vehiculo.correo }}</td>
                <td>
                  <div class="btn-group" role="group">
                    <button type="button" class="btn btn-info">
                      Actualizar
                    </button>
                    <button type="button" class="btn btn-danger">
                      Eliminar
                    </button>
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

<script>
import axios from "axios";
export default {
  data() {
    return {
      vehiculos: [],
      addVehiculoForm: {
        marca: "",
        modelo: "",
        placa: "",
        color: "",
        tipo_vehiculo: "",
      },
    };
  },

  methods: {
    getVehiculos() {
      const path = "http://localhost:5000/vehiculos";
      axios
        .get(path)
        .then((res) => {
          this.vehiculos = res.data;
        })
        .catch((err) => {
          console.error(err);
        });
    },
  },
  created() {
    this.getVehiculos();
  },
};
</script>

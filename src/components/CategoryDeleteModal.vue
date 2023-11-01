<template>
    <div class="modal fade" id="modalTest" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="staticBackdropLabel">Add Product</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <p>lorem ipsum</p>
          </div>
          <div class="modal-footer text-center">
            <button type="button" class="btn btn-sm btn-outline-success" @click="deleteCategory">
              <span v-if="loading" class="spinner-border spinner-border-sm"></span>
              Add
            </button>
            <button type="button" class="btn btn-sm btn-outline-danger" id="productModalClose" data-bs-dismiss="modal">Close</button>
          </div>
          <div class="row d-flex justify-content-center" v-if="errordata.isError">
            <div class="col-11 text-center">
              <div class="alert alert-danger" role="alert">
                {{ errordata.msg }}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
</template>

<script setup>
import { ref, reactive } from 'vue';
// import axiosClient from '@/js/axios.js'
const props = defineProps({
  name: {
      type: String,
      required: true,
  },
  id: {
        type: Number,
        required: true,
  }
})

const loading = ref(false)

const errordata = reactive({
  isError: false,
  msg: "",
})


// onMounted(() => {
//     const myModalEl = document.getElementById('modalCategoryDelete')
//     myModalEl.addEventListener('show.bs.modal', event => {
//     // console.log(props)
//     console.log(id)
//     console.log(name)
// })

const deleteCategory = () => {
    console.log(props)
}

// const handleDelete = async() => {
//     console.log('Delete Category: ', props.id)
//     try {
//         const res = await axiosClient.delete(`/api/category/${props.id}`)
//         console.log(res)
//         // window.location.reload()
//         document.getElementById('modalCategoryDeleteClose').click()
//     } catch (error) {
//         console.log('Error: ', error)
//         errordata.isError = true,
//         errordata.msg = error.data.message
//     }

// }   
</script>

<style scoped></style>
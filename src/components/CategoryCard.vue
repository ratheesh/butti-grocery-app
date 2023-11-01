<template>
  <div class="card border-secondary m-2 p-0 pb-2" style="width: 20rem;">
  <div class="card-body p-0">
    <img :src='img_src' class="card-img-top object-fit-fit" alt="Category Image">
    <h5 class="card-title text-center">{{ props.category.name }}</h5>
    <div class="d-flex justify-content-around">
        <button class="btn btn-sm btn-success">
            <mdicon name="cog" class="text-white" :size='20' />
            Manage
        </button>
        <button class="btn btn-sm btn-info">
            <mdicon name="pencil-box-outline" class="text-danger" :size='20' />
            Edit
        </button>
        <button class="btn btn-sm btn-danger" data-bs-toggle='modal' data-bs-target="#modalCategoryDelete">
            <mdicon name="delete" class="text-white" :size='20' />
            Delete
        </button>
    </div>
  </div>
  <!-- <pre>{{ props }}</pre> -->
    <!-- <pre>{{ props.category.id }}</pre> -->
<!-- <CategoryDeleteModal :id="id" :name="props.category.name" /> -->
</div> 

<!-- Category delete modal -->
  <div class="modal fade" id="modalCategoryDelete" tabindex="-1" aria-labelledby="modalCategoryDeleteLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h2 class="modal-title fs-5" id="modalCategoryDeleteLabel">Delete Category</h2>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <p>
            <b>Deleting category will delete all the products associated with this category.</b>
            Do you want to delete category <b>`${props.category.name}`</b>?
          </p>
            <pre>{{ props }}</pre>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-danger" @click="handleDelete($props.category.id)">Delete {{ props.category.id }}</button>
          <button type="button" class="btn btn-secondary" id='modalCategoryDeleteClose' data-bs-dismiss="modal">Cancel</button>
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
import { ref, reactive, onMounted } from 'vue';
// import CategoryDeleteModal from '@/components/CategoryDeleteModal.vue';
// import axiosClient from '@/js/axios.js';

const props = defineProps({
  category: {
    id: {
        type: Number,
        required: true,
    },
    name: {
        type: String,
        required: true,
    },
    image: {
        type: String,
        required: true,
    },
    created_timestamp: {
        type: String,
        required: true,
    },
  },
})

// onMounted(() =>{
//     console.log(props.category.id)
// })

const errordata = reactive({
    isError : false,
    msg : ''
})

const img_src=`http://127.0.0.1:5000/images/category/${props.category.image}`

const id=ref(props.category.id)

const handleDelete =(id) => {
    // console.log('from function:', get_category_id())
    console.log('param:', id)
    console.log('Delete Category: ', props.category.name)
    console.log(props.category.id)

    // try {
    //     console.log('modal: category id:', props.category.id, id)
    //     const res = await axiosClient.delete(`/api/category/${props.category.id}`)
    //     console.log(res)
    //     // window.location.reload()
    //     document.getElementById('modalCategoryDeleteModal').click()
    //     errordata.isError = false,
    //     errordata.msg = ''
    // } catch (error) {
    //     console.log('Error: ', error)
    //     errordata.isError = true,
    //     errordata.msg = error.message
    // }
}

</script>

<style scoped>
.card-img-top {
    width: 100%;
    height: 150px;
};
</style>
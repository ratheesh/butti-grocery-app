<template>
  <form-layout>
    <div class="container">
      <div class="row justify-content-center mb-3">
        <div class="col-md-6">
          <div class="card shadow-sm m-auto">
            <h3 class="text-center mt-2">Signup</h3>
            <hr />
            <div class="card-body m-0 p-0">
              <form m-0 @submit.prevent="handleSignup">
                <div class="row justify-content-center m-0 p-0">
                  <div class="col-md-10 m-0 p-0">
                    <div class="form-group mb-3">
                      <label for="name"
                        >Full Name<span class="text-danger"><b>*</b></span></label
                      >
                      <div class="input-group">
                        <span class="input-group-text" id="user">
                          <mdicon name="form-textbox" :size="20" />
                        </span>
                        <input
                          type="text"
                          :class="{ 'form-control':true, 'is-invalid':errors.name }"
                          placeholder="Kumar"
                          id="name"
                          v-model="userdata.name"
                          autofocus
                        />
                      </div>
                    </div>
                    <div class="form-group mb-4">
                      <label for="username"
                        >User Name<span class="text-danger"><b>*</b></span></label
                      >
                      <div class="input-group">
                        <span class="input-group-text" id="username">
                          <mdicon name="account" :size="20" />
                        </span>
                        <input
                          type="text"
                          class="form-control"
                          placeholder="username"
                          id="username"
                          :class="{ 'form-control':true, 'is-invalid':errors.username }"
                          v-model="userdata.username"
                          autofocus
                        />
                      </div>
                    </div>
                    <div class="form-group mb-3">
                      <label for="email"
                        >E-Mail<span class="text-danger"><b>*</b></span></label
                      >
                      <div class="input-group">
                        <span class="input-group-text" id="username">
                          <mdicon name="email" :size="20" />
                        </span>
                        <input
                          type="text"
                          id="email"
                          class="form-control"
                          placeholder="username@user.com"
                          :class="{ 'form-control':true, 'is-invalid':errors.email }"
                          v-model="userdata.email"
                        />
                      </div>
                    </div>
                    <div class="form-group mb-3">
                      <label for="role"
                        >User Role<span class="text-danger"><b>*</b></span></label
                      >
                      <div class="input-group">
                        <span class="input-group-text" id="username">
                          <mdicon name="security" :size="20" />
                        </span>
                        <select
                          name="role"
                          id="role"
                          class="form-control"
                          :class="{ 'form-control':true, 'is-invalid':errors.role }"
                          v-model="userdata.role"
                        >
                          <option v-for="(option, idx) in options" :key="idx" :value="option">
                            {{ option }}
                          </option>
                        </select>
                      </div>
                    </div>
                    <div class="form-group mb-3">
                      <label for="password"
                        >Password<span class="text-danger"><b>*</b></span></label
                      >
                      <div class="input-group">
                        <span class="input-group-text" id="username">
                          <mdicon name="form-textbox-password" :size="20" />
                        </span>
                        <input
                          type="password"
                          :class="{ 'form-control':true, 'is-invalid':errors.password }"
                          v-model="userdata.password"
                          id="password"
                          class="form-control"
                          placeholder="Enter Password"
                        />
                      </div>
                    </div>
                    <div class="form-group mb-3">
                      <label for="password2"
                        >Re-enter Password<span class="text-danger"><b>*</b></span></label
                      >
                      <div class="input-group">
                        <span class="input-group-text" id="username">
                          <mdicon name="form-textbox-password" :size="20" />
                        </span>
                        <input
                          type="password"
                          :class="{ 'form-control':true, 'is-invalid':errors.password }"
                          v-model="userdata.password2"
                          id="password2"
                          class="form-control"
                          placeholder="Re-enter Password"
                        />
                      </div>
                    </div>
                  </div>
                </div>
                <hr class="mt-1 mx-0" />
                <div class="mb-3 text-center">
                  <button type="submit" class="btn btn-sm btn-outline-primary">
                    <span v-if="loading" class="spinner-border spinner-border-sm"></span>
                    <span v-if="!loading"><mdicon name="account-plus" :size="25" /></span>
                    Signup
                  </button>
                  &nbsp;
                  <span class="text-muted">Already a Member?</span>
                  &nbsp;
                  <a @click.prevent="handleLogin" href="#">Login</a>
                </div>
              </form>
              <div class="alert alert-danger mx-3 text-center" role="alert" v-if="errorinfo.iserr">
                {{ errorinfo.errmsg }}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </form-layout>
</template>

<script setup>
import { ref, reactive } from 'vue'
import axiosClient from '@/js/axios.js'
import { useRouter } from 'vue-router'
import FormLayout from '@/layouts/FormLayout.vue'

const options = ['user', 'manager']

const userdata = reactive({
  name: '',
  username: '',
  email: '',
  role: 'user',
  password: '',
  password2: ''
})

const errorinfo = reactive({
  iserr: false,
  errmsg: ''
})

const loading = ref(false)
const iserr = ref(false)
const errmsg = ref('')
const errors = reactive({
  name:false,
  username: false,
  email:false,
  role: false,
  password: false,
})

const router = useRouter()

const handleSignup = async () => {
  errorinfo.iserr = false
  errorinfo.errmsg = ''

  if (userdata.password != userdata.password2) {
    iserr.value = true
    errmsg.value = 'Password does not match'
    userdata.password = userdata.password2 = ''
    return
  }

    const formData = new FormData()
    formData.append('name', userdata.name)
    formData.append('username', userdata.username)
    formData.append('email', userdata.email)
    formData.append('role', userdata.role)
    formData.append('password', userdata.password)
    formData.append('image_name', 'default.png')

    loading.value = true
    try {
      const res = await axiosClient.post('/api/user', formData)
      console.log(res)
      if (res.status == 201)
       console.log(`user ${userdata.username} signed up!`)
      else {
        console.log('Signup Error')
        errorinfo.iserr = true
        errorinfo.errmsg = res.data
        errors.name = errorinfo.errmsg.includes('name')
        errors.username = errorinfo.errmsg.includes('user')
        errors.email = errorinfo.errmsg.includes('email')
        errors.password = errorinfo.errmsg.includes('password')
      }
    } catch (err) {
      console.log(err)
        errorinfo.iserr = true
        errorinfo.errmsg = err.response.data
        errors.name = errorinfo.errmsg.includes('name')
        errors.username = errorinfo.errmsg.includes('user')
        errors.email = errorinfo.errmsg.includes('email')
        errors.password = errorinfo.errmsg.includes('password')
    } finally {
      loading.value = false
    }
  }

const handleLogin = () => {
  router.push('/login')
}
</script>

<style scoped></style>

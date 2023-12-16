<template>
  <form-layout>
    <div class="container">
      <div class="row justify-content-center vh-auto">
        <div class="col-md-6">
          <div
            class="row col-md-12 col-lg-12 m-auto mt-3 px-0 d-inline-flex justify-content-center"
          >
            <div class="col-8 d-flex align-items-end justify-content-center">
              <mdicon name="basket" class="text-center text-primary mx-2" height="90" width="90" />
            </div>
          </div>
          <div class="card shadow-sm m-auto">
            <h3 class="text-center mt-2">Signup</h3>
            <hr />
            <div class="card-body m-0 p-0">
              <form
                m-0
                @submit.prevent="handleSignup"
                needs-validation
                novalidate
                :class="{ 'was-validated': wasValidated }"
              >
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
                          class="form-control rounded-end"
                          :class="{ 'form-control': true, 'is-invalid': errors.name }"
                          placeholder="Kumar"
                          id="name"
                          v-model="userdata.name"
                          autofocus
                        />
                        <div class="invalid-feedback">
                          <span>Enter a valid Name</span>
                        </div>
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
                          class="form-control rounded-end"
                          placeholder="username"
                          id="username"
                          :class="{ 'form-control': true, 'is-invalid': errors.username }"
                          v-model="userdata.username"
                          autofocus
                        />
                        <div class="invalid-feedback">
                          <span>Enter a valid Username</span>
                        </div>
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
                          class="form-control rounded-end"
                          placeholder="username@user.com"
                          :class="{ 'form-control': true, 'is-invalid': errors.email }"
                          v-model="userdata.email"
                        />
                        <div class="invalid-feedback">
                          <span>Enter a valid E-Mail</span>
                        </div>
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
                          class="form-control rounded-end"
                          :class="{ 'form-control': true, 'is-invalid': errors.role }"
                          v-model="userdata.role"
                        >
                          <option v-for="(option, idx) in options" :key="idx" :value="option">
                            {{ option }}
                          </option>
                        </select>
                        <div class="invalid-feedback">
                          <span>Enter a valid Role</span>
                        </div>
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
                          :class="{ 'form-control': true, 'is-invalid': errors.password }"
                          v-model="userdata.password"
                          id="password"
                          class="form-control rounded-end"
                          placeholder="Enter Password"
                        />
                        <div class="invalid-feedback">
                          <span>Enter valid Password</span>
                        </div>
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
                          :class="{ 'form-control': true, 'is-invalid': errors.password }"
                          v-model="userdata.password2"
                          id="password2"
                          class="form-control rounded-end"
                          placeholder="Re-enter Password"
                        />
                        <div class="invalid-feedback">
                          <span>Enter valid Password</span>
                        </div>
                      </div>
                    </div>
                    <div class="mb-2">
                      <input
                        type="file"
                        class="form-control"
                        id="profileImage"
                        placeholder="Profile Image"
                        accept="image/png, image/jpeg"
                        value=""
                        @change="handleImage"
                      />
                    </div>
                  </div>
                </div>
                <hr class="mt-1 mx-0" />
                <div class="mb-3 text-center">
                  <a
                    href="javascript:void(0)"
                    class="btn btn-sm btn-secondary d-inline-flex align-items-center mx-2"
                    @click="router.push('/')"
                  >
                    <span class="mx-1"><mdicon name="home" :size="18" /></span>
                    <span>Home</span>
                  </a>
                  <button type="submit" class="btn btn-sm btn-primary mx-2">
                    <span v-if="loading" class="spinner-border spinner-border-sm"></span>
                    <span v-if="!loading"><mdicon name="account-plus" :size="18" /></span>
                    Signup
                  </button>
                  <span class="text-muted">Already a Member?</span>
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
  password2: '',
  image: null,
  image_name: null
})

const errorinfo = reactive({
  iserr: false,
  errmsg: ''
})

const loading = ref(false)
const errors = reactive({
  name: false,
  username: false,
  email: false,
  role: false,
  password: false
})
const wasValidated = ref(false)

const router = useRouter()

const handleImage = (e) => {
  console.log('modal: handle Image')
  // console.log(e)
  if (e.target.files.length === 0) {
    console.log('cancel file selection')
    userdata.image_name = null
    userdata.image = null
    return
  }

  userdata.image = e.target.files[0]
  userdata.image_name = userdata.image.name
  console.log(userdata.image)
  createBase64Image(userdata.image)
}

function createBase64Image(fObj) {
  const reader = new FileReader()
  reader.onload = (e) => {
    userdata.image = e.target.result.split(',')[1]
  }
  reader.readAsDataURL(fObj)
}

const validateEmail = (email) => {
  var re = /\S+@\S+\.\S+/
  return re.test(email)
}

const handleSignup = async () => {
  errorinfo.iserr = false
  errorinfo.errmsg = ''
  errors.name = false
  errors.username = false
  errors.email = false
  errors.role = false
  errors.password = false

  wasValidated.value = false

  if (!validateEmail(userdata.email)) {
    errors.email = true
    return
  }

  if (
    !userdata.name ||
    !userdata.username ||
    !userdata.email ||
    !userdata.role ||
    !userdata.password ||
    !userdata.password2
  ) {
    // errorinfo.iserr = true
    // errorinfo.errmsg = 'Invalid user data'
    errors.name = !userdata.name
    errors.username = !userdata.username
    errors.email = !userdata.email
    errors.role = !userdata.role
    errors.password = !userdata.password
    return
  }
  if (userdata.password !== userdata.password2) {
    errorinfo.iserr = true
    errorinfo.errmsg = 'Passwords does not match'
    userdata.password = userdata.password2 = ''
    errors.password = true
    return
  }

  wasValidated.value = true

  const formData = new FormData()
  formData.append('name', userdata.name)
  formData.append('username', userdata.username)
  formData.append('email', userdata.email)
  formData.append('role', userdata.role)
  formData.append('password', userdata.password)
  if (userdata.image_name !== null) formData.append('image_name', userdata.image_name)
  if (userdata.image !== null) formData.append('image', userdata.image)

  loading.value = true
  try {
    const res = await axiosClient.post('/api/user', formData)
    console.log(res)
    if (res.status == 201) {
      console.log(`user ${userdata.username} signed up!`)
      router.push('/login')
    } else {
      console.log('Signup Error')
      errorinfo.iserr = true
      errorinfo.errmsg = res.data
      errors.name = errorinfo.errmsg.includes('name')
      errors.username = errorinfo.errmsg.includes('user')
      errors.email = errorinfo.errmsg.includes('email')
      errors.password = errorinfo.errmsg.includes('password')
    }
  } catch (err) {
    // console.log(err)
    wasValidated.value = false
    errorinfo.iserr = true
    errorinfo.errmsg = err.response.data
    errors.name = errorinfo.errmsg.includes('name')
    errors.username = errorinfo.errmsg.includes('username')
    errors.email = errorinfo.errmsg.includes('email')
    errors.password = errorinfo.errmsg.includes('password')
    errors.role = errorinfo.errmsg.includes('role')
  } finally {
    loading.value = false
  }
}

const handleLogin = () => {
  router.push('/login')
}
</script>

<style scoped></style>

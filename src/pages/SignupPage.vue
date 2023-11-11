<template>
  <form-layout>
    <div class="container">
      <div class="row justify-content-md-center">
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
                          class="form-control"
                          placeholder="Kumar"
                          id="name"
                          v-model="userdata.name"
                          autofocus
                          required
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
                          v-model="userdata.username"
                          autofocus
                          required
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
                          v-model="userdata.email"
                          required
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
                          required="yes"
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
              <div class="alert alert-danger mx-3 text-center" role="alert" v-if="iserr">
                {{ errmsg }}
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
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/authstore.js'
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

const router = useRouter()
const auth = useAuthStore()

const handleSignup = async () => {
  if (userdata.password != userdata.password2) {
    iserr.value = true
    errmsg.value = 'Password does not match'
    userdata.password = userdata.password2 = ''
    return
  }

  try {
    loading.value = true
    const res = await auth.signup(userdata)
    console.log('signup page: ', res)
    console.log('status code:', res.status)
    if (res.status == 201) {
      if (auth.user.role == 'admin') router.push('/admin')
      else if (auth.user.role == 'manager') router.push('/manager')
      else router.push('/')
    } else {
      console.log('Return code is not 201')
    }
  } catch (err) {
    errorinfo.iserr = true
    errorinfo.errmsg = err.data
  } finally {
    loading.value = false
  }
}

const handleLogin = () => {
  router.push('/login')
}
</script>

<style scoped></style>

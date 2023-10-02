<template>
  <div class="container">
    <div class="row justify-content-md-center mt-5">
      <div class="col-md-5">
        <div class="card m-auto">
          <h2 class="text-center my-3">Signup</h2>
          <hr />
          <div class="card-body m-0 p-0">
            <form m-0>
              <div class="mb-3 px-3">
                <label for="user" class="form-label">Name</label>
                <input type="text" id="user" class="form-control" placeholder="Name" />
              </div>
              <div class="mb-3 px-3">
                <label for="username" class="form-label">User Name</label>
                <input
                  type="text"
                  id="username"
                  class="form-control"
                  placeholder="User Name"
                />
              </div>
              <div class="mb-3 px-3">
                <label for="email" class="form-label">E-Mail</label>
                <input
                  type="text"
                  id="email"
                  class="form-control"
                  placeholder="E-mail address"
                />
              </div>
              <div class="mb-3 px-3">
                <label for="role" class="form-label">Role</label>
                <select
                  name="role"
                  id="role"
                  class="form-control"
                  type="text"
                  required="yes"
                >
                  <option value="user">User</option>
                  <option value="manager">Manager</option>
                </select>
              </div>
              <div class="mb-3 px-3">
                <label for="password" class="form-label">Password</label>
                <input
                  type="password"
                  id="password"
                  class="form-control"
                  placeholder="Password"
                />
              </div>
              <div class="mb-3 px-3">
                <label for="password2" class="form-label">Re-enter Password</label>
                <input
                  type="password2"
                  id="password2"
                  class="form-control"
                  placeholder="Password"
                />
              </div>
              <hr class="mt-3 mx-0" />
              <div class="mb-3 text-center">
                <button
                  type="submit"
                  @click.prevent="handleSignup"
                  class="btn btn-success"
                >
                  <mdicon name="account-plus" :size="25" />
                  Signup
                </button>
                &nbsp;
                <span class="text-muted">Already a Member?</span>
                &nbsp;
                <a @click.prevent="handleLogin" href="#">Login</a>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import router from "@/router";

const handleSignup = () => {
  console.log("Signup");
  router.push("/signup");
};

const handleLogin = () => {
  console.log("Login");
  router.push("/login");
};
</script>

<style scoped></style>

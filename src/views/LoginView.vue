<template>
  <div class="container">
    <div class="row justify-content-md-center mt-5">
      <div class="col-md-5">
        <div class="card m-auto">
          <h2 class="text-center my-3">Login</h2>
          <hr />
          <div class="card-body m-0 p-0">
            <form m-0>
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
                <label for="password" class="form-label">Password</label>
                <input
                  type="password"
                  id="password"
                  class="form-control"
                  placeholder="Enter password"
                />
              </div>
              <hr class="mt-3 mx-0" />
              <div class="mb-3 text-center">
                <button
                  type="submit"
                  @click.prevent="handleLogin"
                  class="btn btn-success btn-sm"
                >
                  Login
                </button>
                &nbsp;
                <span class="text-muted">Not a Member?</span>
                &nbsp;
                <a @click.prevent="gotoSignup" href="">Signup</a>
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

const gotoSignup = () => {
  console.log("Signup");
  router.push("/signup");
};

const handleLogin = () => {
  console.log("Login");
  router.push("/login");
};
</script>

<style scoped></style>

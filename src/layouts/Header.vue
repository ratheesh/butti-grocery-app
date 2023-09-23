<template>
  <nav class="navbar sticky-top navbar-expand-lg bg-body-tertiary">
    <div class="container-fluid text-white" style="background-color: #34495e">
      <router-link to="/" class="navbar-brand text-white">
        <div class="align-items-center">
          <mdicon name="basket" class="text-white color-success" :size="30" />
          <span class="fs-3">Butti</span>
        </div>
      </router-link>
      <div>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <form class="d-flex" role="search">
            <input
              class="form-control me-2 border-2"
              type="search"
              placeholder="Search"
              aria-label="Search"
            />
            <button class="btn btn-outline-success" type="submit">
              <mdicon name="magnify" :size="30" />
            </button>
          </form>
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item mx-1">
              <router-link to="/" class="nav-link">
                <mdicon class="text-white" name="home" :size="30" />
              </router-link>
            </li>
            <li class="nav-item mx-1">
              <router-link to="/signup" class="nav-link">
                <mdicon class="text-white" name="account-plus" :size="30" />
              </router-link>
            </li>
            <li class="nav-item mx-1">
              <router-link
                to="/cart"
                data-bs-toggle="offcanvas"
                data-bs-target="#offcanvasRight"
                class="nav-link"
              >
                <mdicon name="cart" class="text-white" :size="30" />
                <span class="badge text-bg-warning">4</span>
              </router-link>
            </li>
            <li class="nav-item mx-1">
              <router-link to="/login" class="nav-link">
                <mdicon name="login" class="text-white" :size="30" />
              </router-link>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { RouterLink } from "vue-router";
</script>

<style scoped></style>

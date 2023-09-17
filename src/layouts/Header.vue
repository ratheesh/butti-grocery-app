<template>
<nav class="navbar sticky-top navbar-expand-lg bg-body-tertiary">
    <div class="container-fluid">
        <router-link to="/" class="navbar-brand">Butti</router-link>
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
        <div>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <form class="d-flex" role="search">
                <input
                class="form-control me-2 border-2"
                type="search"
                placeholder="Search"
                aria-label="Search"
                />
                <button class="btn btn-outline-success" type="submit">Search</button>
            </form>
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                <li class="nav-item mx-1">
                    <router-link to="/" class="nav-link">Home</router-link>
                </li>
                <li class="nav-item mx-1">
                    <router-link to="/login" class="nav-link">Login</router-link>
                </li>
                <li class="nav-item mx-1">
                    <router-link to="/signup" class="nav-link">SignUp</router-link>
                </li>
            </ul>
        </div></div>
    </div>
</nav>
<router-view></router-view>
</template>

<script setup>
import { RouterLink, RouterView } from "vue-router";
</script>

<style scoped>

</style>
<script lang="ts">
	import { authenticated } from "../stores/auth";
	let auth = false;
	authenticated.subscribe((a) => (auth = a));
</script>

{#if auth}
	<a href="/">home</a>
	<a href="/register">logout</a>
	<slot />
{:else}
	<a href="/">Home</a>
	<a href="/register">Register</a>
	<a href="/login">Login</a>
	<slot />
{/if}

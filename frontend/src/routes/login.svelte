<script lang="ts">
	import { authenticated } from "../stores/auth";
	import { goto } from "$app/navigation";

	let username: string, password: string;
	const submit = async () => {
		const searchParameters = new URLSearchParams();
		searchParameters.append("username", username);
		searchParameters.append("password", password);
		const response = await fetch("http://127.0.0.1:8000/login", {
			method: "POST",
			credentials: "include",
			headers: { "Content-Type": "application/x-www-form-urlencoded" },
			body: searchParameters.toString()
		});
		const data = await response.json();
		localStorage.setItem("token", data.token);
		authenticated.set(true);
		goto("/");
	};
</script>

<form on:submit|preventDefault={submit}>
	<h1>Login</h1>
	<input bind:value={username} type="text" placeholder="Username" required />
	<input bind:value={password} type="password" placeholder="Password" required />
	<button type="submit">Submit</button>
</form>

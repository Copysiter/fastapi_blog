<script lang="ts">
	let username: string, password: string;
	const submit = async () => {
		await fetch("http://127.0.0.1:8000/register", {
			method: "POST",
			headers: { "Content-Type": "application/json" },
			body: JSON.stringify({
				username,
				password
			})
		});
	};
</script>

<form on:submit|preventDefault={submit}>
	<h1>Register</h1>
	<input bind:value={username} type="text" placeholder="Username" required />
	<input bind:value={password} type="password" placeholder="Password" required />
	<button type="submit">Submit</button>
</form>

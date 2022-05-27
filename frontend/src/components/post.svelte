<div>
	<a href={`/posts/${post.slug}`}>
		<h2>{post.title}</h2>
	</a>
	{post.created_at}
	<div>
		{#each post.categories as category}
			<a href={`/categories/${category}`}>
				<span>{category}</span>
			</a>
		{/each}
	</div>
	<p>{`${post.body.slice(0,400)}...`}</p>
</div>


<script lang="ts">
	import type { Post } from "../stores/posts";
	export let post: Post;
</script>
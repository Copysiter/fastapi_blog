<script lang="ts">
	import type { Post } from "../stores/posts";
	export let post: Post;
</script>

<a href={`/posts/${post.slug}`}><h2>{post.title}</h2></a>
{#each post.categories as category}
<span>{category}</span>
{/each}
<p>{post.body}</p>

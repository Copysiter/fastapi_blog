<script lang="ts">
	import type { Post } from "../stores/posts";
	export let post: Post;
</script>

<a href={`/posts/${post.slug}`}><h2>{post.title}</h2></a>
<p>{post.body}</p>

<div>
	<a href={`/posts/${post.slug}`}>
		<h2>{post.title}</h2>
	</a>
	{post.created_at}
	<div>
			<a href={`/categories/${post.category}`}>
				<span>{post.category}</span>
			</a>
	</div>
	<p>{`${post.body.slice(0,400)}...`}</p>
</div>


<script lang="ts">
	import type { Post } from "../stores/posts";
	export let post: Post;
</script>
Go to [ai.azure.com](https://ai.azure.com/) and login to your account
![Alt text](https://github.com/innovationlabOBS/gen-ai-introduction/blob/main/Images%20Files/Azure%20Prompt%20Flow/intro.png?raw=true "Intro")

Click on New project to create a project
![Alt text](https://github.com/innovationlabOBS/gen-ai-introduction/blob/main/Images%20Files/Azure%20Prompt%20Flow/create%20project.png?raw=true "Create Project")

Fill out the fields (default values will be fine)
![Alt text](https://github.com/innovationlabOBS/gen-ai-introduction/blob/main/Images%20Files/Azure%20Prompt%20Flow/create%20hub.png?raw=true "Create Hub")

For Connect Azure AI Search, click Create new AI search and enter a name
![Alt text](https://github.com/innovationlabOBS/gen-ai-introduction/blob/main/Images%20Files/Azure%20Prompt%20Flow/create%20new%20ai%20search.png?raw=true "Create New AI Search")

Click next, review, then click Create a project
![Alt text](https://github.com/innovationlabOBS/gen-ai-introduction/blob/main/Images%20Files/Azure%20Prompt%20Flow/review%20and%20finish.png?raw=true "Review and Finish")

On the left panel, click on prompt flow
![Alt text](https://github.com/innovationlabOBS/gen-ai-introduction/blob/main/Images%20Files/Azure%20Prompt%20Flow/create%20project.png?raw=true "Create Project")

Click Create to create a new flow
![Alt text](https://github.com/innovationlabOBS/gen-ai-introduction/blob/main/Images%20Files/Azure%20Prompt%20Flow/create%20promptflow.png?raw=true "Create Promptflow")

Clone the Multi Round Q&A on you data
![Alt text](https://github.com/innovationlabOBS/gen-ai-introduction/blob/main/Images%20Files/Azure%20Prompt%20Flow/create%20chat%20flow.png?raw=true "Create Chat Flow")

Choose a folder name or use the default, and click Clone
![Alt text](https://github.com/innovationlabOBS/gen-ai-introduction/blob/main/Images%20Files/Azure%20Prompt%20Flow/clone%20multiround.png?raw=true "Clone Multi Round")

On the left hand panel, click Deployments
![Alt text](https://github.com/innovationlabOBS/gen-ai-introduction/blob/main/Images%20Files/Azure%20Prompt%20Flow/prompt%20flow%20created.png?raw=true "Promptflow Created")

Click Deploy a model
![Alt text](https://github.com/innovationlabOBS/gen-ai-introduction/blob/main/Images%20Files/Azure%20Prompt%20Flow/deploy%20model.png?raw=true "Deploy Model")

Choose GPT-4o chat completion and click confirm (or another chat completion model of your choice)
![Alt text](https://github.com/innovationlabOBS/gen-ai-introduction/blob/main/Images%20Files/Azure%20Prompt%20Flow/select%20a%20model.png?raw=true "Select a Model")

Choose a deployment name and click Deploy
![Alt text](https://github.com/innovationlabOBS/gen-ai-introduction/blob/main/Images%20Files/Azure%20Prompt%20Flow/deploy%20gpt-4o.png?raw=true "Deploy GPT4o")

On the left hand panel click Indexes
![Alt text](https://github.com/innovationlabOBS/gen-ai-introduction/blob/main/Images%20Files/Azure%20Prompt%20Flow/gpt%204-o%20deployment%20info.png?raw=true "GPT4o Development Info")

Click on New index
![Alt text](https://github.com/innovationlabOBS/gen-ai-introduction/blob/main/Images%20Files/Azure%20Prompt%20Flow/indexes.png?raw=true "Indexes")

Click Upload files and upload some PDF or text files you want to use for RAG, then click Next
![Alt text](https://github.com/innovationlabOBS/gen-ai-introduction/blob/main/Images%20Files/Azure%20Prompt%20Flow/create%20index%20file%20upload.png?raw=true "Create Index File Upload")

Under Select Azure AI Search service, click Connect other Azure AI Search resource
![Alt text](https://github.com/innovationlabOBS/gen-ai-introduction/blob/main/Images%20Files/Azure%20Prompt%20Flow/connect%20other%20ai%20search.png?raw=true "Connect Other AI Search")

Click Add connection
![Alt text](https://github.com/innovationlabOBS/gen-ai-introduction/blob/main/Images%20Files/Azure%20Prompt%20Flow/add%20connection.png?raw=true "Add Connection")

The connection will automatically be added. Click next
![Alt text](https://github.com/innovationlabOBS/gen-ai-introduction/blob/main/Images%20Files/Azure%20Prompt%20Flow/finish%20create%20index.png?raw=true "Finish Create Index")

Embedding model will be automatically selected. Click next
![Alt text](https://github.com/innovationlabOBS/gen-ai-introduction/blob/main/Images%20Files/Azure%20Prompt%20Flow/search%20settings.png?raw=true "Search Settings")

Review and click Create
![Alt text](https://github.com/innovationlabOBS/gen-ai-introduction/blob/main/Images%20Files/Azure%20Prompt%20Flow/review%20and%20create%20index.png?raw=true "Review and Create Index")

Wait until all the processes have completed, and go to Prompt flow on the left panel
![Alt text](https://github.com/innovationlabOBS/gen-ai-introduction/blob/main/Images%20Files/Azure%20Prompt%20Flow/completed%20indexes.png?raw=true "Completed Indexes")

In the Modify query with history tab, set the connection to the embedding model that was created
![Alt text](https://github.com/innovationlabOBS/gen-ai-introduction/blob/main/Images%20Files/Azure%20Prompt%20Flow/prompt%20flow%20modify%20query%20with%20history.png?raw=true "Promptflow Modify Query With History")

Set the deployment name to the LLM model that was deployed
![Alt text](https://github.com/innovationlabOBS/gen-ai-introduction/blob/main/Images%20Files/Azure%20Prompt%20Flow/set%20model%20and%20params.png?raw=true "Set Model and Params")

In the lookup tab, click on the mlindex_content value input
![Alt text](https://github.com/innovationlabOBS/gen-ai-introduction/blob/main/Images%20Files/Azure%20Prompt%20Flow/start%20compute%20session.png?raw=true "Start Compute Session")

For index_type, click Registered index
![Alt text](https://github.com/innovationlabOBS/gen-ai-introduction/blob/main/Images%20Files/Azure%20Prompt%20Flow/lookup%20mlindex%20content%20reg%20index.png?raw=true "Lookup ML Index Content Register Index")

For mlindex_asset_id, select the index that was generated, click Save
![Alt text](https://github.com/innovationlabOBS/gen-ai-introduction/blob/main/Images%20Files/Azure%20Prompt%20Flow/asset%20id.png?raw=true "Asset ID")

For query_type, select Hybrid(vector + keyword)
![Alt text](https://github.com/innovationlabOBS/gen-ai-introduction/blob/main/Images%20Files/Azure%20Prompt%20Flow/query%20type%20hybrid%20keyword%20vector.png?raw=true "Query Type Hybrid Vector Keyword")

Go to the prompt variants tab
![Alt text](https://github.com/innovationlabOBS/gen-ai-introduction/blob/main/Images%20Files/Azure%20Prompt%20Flow/show%20prompt%20variants.png?raw=true "Show Prompt Variants")

For this simple example, we don't need the variants, so delete them, only leaving the first one
![Alt text](https://github.com/innovationlabOBS/gen-ai-introduction/blob/main/Images%20Files/Azure%20Prompt%20Flow/delete%20variants.png?raw=true "Delete Variants")

Go to the chat with context tab and add the generated embedding model to the connection
![Alt text](https://github.com/innovationlabOBS/gen-ai-introduction/blob/main/Images%20Files/Azure%20Prompt%20Flow/chat%20with%20context%20add%20connection.png?raw=true "Chat with Context add Connection")

Under deployment name, select the LLM model, then click on Chat in the upper right corner
![Alt text](https://github.com/innovationlabOBS/gen-ai-introduction/blob/main/Images%20Files/Azure%20Prompt%20Flow/chat%20with%20context%20add%20deployment.png?raw=true "Chat with Context add Deployment")

Enter a query relavant to your RAG documents
![Alt text](https://github.com/innovationlabOBS/gen-ai-introduction/blob/main/Images%20Files/Azure%20Prompt%20Flow/chat.png?raw=true "Chat")

The model should respond with an answer and a reference to the document
![Alt text](https://github.com/innovationlabOBS/gen-ai-introduction/blob/main/Images%20Files/Azure%20Prompt%20Flow/chat%20output.png?raw=true "Chat Output")
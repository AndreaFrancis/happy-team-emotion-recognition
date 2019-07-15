USE [HappyTeam]
GO

INSERT INTO [dbo].[Sentiments]
           ([SentimentId]
           ,[SentimentName])
     VALUES
           (1, 'angry'),
		   (2, 'disgusted'),
		   (3, 'fearful'),
		   (4, 'happy'),
		   (5, 'sad'),
		   (6, 'surprised'),
		   (7, 'neutral')
GO
